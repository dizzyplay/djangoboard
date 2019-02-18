from .settings import *
import os
import json

DEBUG = True

# sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', None),
        'USER': os.environ.get('DB_USER', None),
        'PASSWORD': os.environ.get('DB_PASSWORD', None),
        'HOST': 'localhost',
    },
}

# 메일 설정 비밀키 윈도우에서  json파일 가져오기
# try:
#     with open(BASE_DIR+"\secret.json","r") as f:
#         secrets = json.loads(f.read())
#     email_host_user=secrets["EMAIL_HOST_USER"]
#     email_host_password=secrets["EMAIL_HOST_PASSWORD"]
# except:#리눅스/맥에서 환경변수로 메일설정 비밀키 가져오기

email_host_user = os.environ.get("EMAIL_HOST_USER", "")
email_host_password = os.environ.get("EMAIL_USER_PASSWORD", "")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = email_host_user

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    '127.0.0.1:8000',
    'localhost:3000',
    'www.rasbp.site',
    'localhost:8080',
)
