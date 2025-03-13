"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import env_config  # type: ignore
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")

print("ASGI: ", os.environ.get("DJANGO_SETTINGS_MODULE"))


application = get_asgi_application()
