from .base import *

RUNTIME = "prod"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://commeta.uz"]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.commeta\.uz$",
    "https://commeta.uz",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]

# REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
#     "rest_framework.renderers.JSONRenderer",
# ]
