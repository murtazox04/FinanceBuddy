import polib
import asyncio
import logging
import subprocess
import re
from pathlib import Path
from typing import List
from dataclasses import dataclass, field
from googletrans import Translator

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class TranslationConfig:
    """Configuration for translation process"""

    languages: List[str] = field(default_factory=lambda: ["en", "ru", "uz"])
    source_lang: str = "en"
    domain: str = "messages"
    locales_dir: str = "locales"

    def __post_init__(self):
        self.locales_path = Path(self.locales_dir)


class TranslationManager:
    def __init__(self, config: TranslationConfig):
        self.config = config
        self.translator = Translator()
        self._ensure_locales_dir()

        # Patterns to identify and protect format strings
        self.format_patterns = [
            r"\{[^}]+\}",  # Named and unnamed format placeholders
            r"%\([^)]+\)[sd]",  # Old-style named placeholders
            r"%[sd]",  # Old-style unnamed placeholders
            r"\{.*?:.+?\}",  # Format specifiers like {:.1f}
        ]

        # Language detection overrides
        self.lang_overrides = {
            "ru": "ru",  # Ensure Russian text is detected as Russian
            "uz": "uz",  # Ensure Uzbek text is detected as Uzbek
        }

    def _ensure_locales_dir(self) -> None:
        """Ensure locales directory exists"""
        self.config.locales_path.mkdir(exist_ok=True)

    def _extract_format_strings(self, text: str) -> tuple[str, list]:
        """Extract format strings and replace with placeholders"""
        format_strings = []
        modified_text = text

        for pattern in self.format_patterns:
            matches = re.finditer(pattern, modified_text)
            for i, match in enumerate(matches):
                placeholder = f"__FORMAT_{i}__"
                format_strings.append(match.group(0))
                modified_text = modified_text.replace(match.group(0), placeholder)

        return modified_text, format_strings

    def _restore_format_strings(self, text: str, format_strings: list) -> str:
        """Restore format strings from placeholders"""
        result = text
        for i, format_string in enumerate(format_strings):
            result = result.replace(f"__FORMAT_{i}__", format_string)
        return result

    def _detect_language(self, text: str) -> str:
        """Detect the language of the text and apply overrides"""
        try:
            detection_result = self.translator.detect(text)
            if isinstance(detection_result, list):
                detected = detection_result[0].lang if detection_result else "en"
            else:
                detected = detection_result.lang
            return self.lang_overrides.get(detected, detected)
        except:
            return "en"

    def _run_command(self, command: str) -> bool:
        """Execute a shell command and handle errors"""
        try:
            process = subprocess.run(
                command, shell=True, check=True, capture_output=True, text=True
            )
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {command}")
            logger.error(f"Error output: {e.stderr}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error running command: {command}")
            logger.error(f"Error: {str(e)}")
            return False

    def extract_messages(self) -> bool:
        """Extract messages from source code"""
        command = (
            "pybabel extract "
            "-k _:1,1t -k _:1,2 -k __ -k gettext -k ngettext "
            f"--input-dirs=. -o {self.config.locales_dir}/messages.pot"
        )
        return self._run_command(command)

    def init_language(self, lang: str) -> bool:
        """Initialize a new language"""
        command = (
            f"pybabel init -i {self.config.locales_dir}/messages.pot "
            f"-d {self.config.locales_dir} -D {self.config.domain} -l {lang}"
        )
        return self._run_command(command)

    def update_translations(self) -> bool:
        """Update existing translations"""
        command = (
            f"pybabel update -i {self.config.locales_dir}/messages.pot "
            f"-d {self.config.locales_dir} -D {self.config.domain}"
        )
        return self._run_command(command)

    def compile_translations(self) -> bool:
        """Compile translations to .mo files"""
        command = (
            f"pybabel compile -d {self.config.locales_dir} -D {self.config.domain}"
        )
        return self._run_command(command)

    async def translate_po_file(self, lang: str) -> None:
        """Translate a .po file for a specific language"""
        if lang == self.config.source_lang:
            return

        po_file = (
            self.config.locales_path / lang / "LC_MESSAGES" / f"{self.config.domain}.po"
        )
        if not po_file.exists():
            logger.error(f"PO file not found: {po_file}")
            return

        try:
            dest_lang = "zh-cn" if lang == "zh" else lang
            po = polib.pofile(str(po_file))

            for entry in po:
                if not entry.msgstr and entry.msgid:
                    try:
                        # Extract format strings before translation
                        modified_text, format_strings = self._extract_format_strings(
                            entry.msgid
                        )

                        # Detect source language to ensure correct translation path
                        detected_lang = self._detect_language(modified_text)
                        if detected_lang and detected_lang != self.config.source_lang:
                            # Two-step translation if needed
                            intermediate_result = self.translator.translate(
                                modified_text,
                                dest=self.config.source_lang,
                                src=detected_lang,
                            )
                            if isinstance(intermediate_result, list):
                                intermediate = (
                                    intermediate_result[0].text
                                    if intermediate_result
                                    else modified_text
                                )
                            else:
                                intermediate = intermediate_result.text

                            translation_result = self.translator.translate(
                                intermediate,
                                dest=dest_lang,
                                src=self.config.source_lang,
                            )

                            if isinstance(translation_result, list):
                                translation = (
                                    translation_result[0].text
                                    if translation_result
                                    else intermediate
                                )
                            else:
                                translation = translation_result.text
                        else:
                            # Direct translation
                            translation_result = self.translator.translate(
                                modified_text,
                                dest=dest_lang,
                                src=self.config.source_lang,
                            )

                            # Handle if result is a list
                            if isinstance(translation_result, list):
                                translation = (
                                    translation_result[0].text
                                    if translation_result
                                    else modified_text
                                )
                            else:
                                translation = translation_result.text

                        # Restore format strings
                        entry.msgstr = self._restore_format_strings(
                            translation, format_strings
                        )

                    except Exception as e:
                        logger.error(f"Translation error for '{entry.msgid}': {str(e)}")

            po.save(str(po_file))
            logger.info(f"Successfully translated {lang}")

        except Exception as e:
            logger.error(f"Error processing {lang}: {str(e)}")

    async def process_all_translations(self) -> None:
        """Process translations for all languages"""
        try:
            logger.info("Extracting messages...")
            if not self.extract_messages():
                return

            for lang in self.config.languages:
                logger.info(f"Processing language: {lang}")
                po_path = (
                    self.config.locales_path
                    / lang
                    / "LC_MESSAGES"
                    / f"{self.config.domain}.po"
                )

                if not po_path.parent.exists():
                    if not self.init_language(lang):
                        continue
                else:
                    if not self.update_translations():
                        continue

                if lang != self.config.source_lang:
                    await self.translate_po_file(lang)

            logger.info("Compiling translations...")
            self.compile_translations()
            logger.info("Translation process completed!")

        except Exception as e:
            logger.error(f"Error in translation process: {str(e)}")


async def main():
    config = TranslationConfig(
        languages=["en", "ru", "uz", "zh"],
        source_lang="en",
        domain="messages",
        locales_dir="locales",
    )

    manager = TranslationManager(config)
    await manager.process_all_translations()


if __name__ == "__main__":
    asyncio.run(main())
