import tempfile

from .base import *


RUNTIME = "test"

DATABASES: dict[str, Any] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "PORT": "5432",
        "TEST": {
            "NAME": "dev_review_test_db",
            "MIGRATE": False,
        },
    }
}

MEDIA_ROOT = tempfile.mkdtemp()
