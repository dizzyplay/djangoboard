import os
from .settings import *
import json

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER':os.environ.get('DATABASE_USER'),
        'PASSWORD':os.environ.get('DATABASE_PASSWORD'),
        'HOST': 'localhost',
    },
}

# 비밀키관련 json파일 불러오기
with open(BASE_DIR + "/secret.json", "r") as f:
    secrets = json.loads(f.read())

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = secrets["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = secrets["EMAIL_HOST_PASSWORD"]
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER