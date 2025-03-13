"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import env_config  # type: ignore
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")

print("WSGI: ", os.environ.get("DJANGO_SETTINGS_MODULE"))


application = get_wsgi_application()
