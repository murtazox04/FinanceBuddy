from .base import *

RUNTIME = "dev"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://3232-194-93-25-162.ngrok-free.app"]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE

INSTALLED_APPS += [
    "debug_toolbar",
]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "dev.commeta.uz"
]


