from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.accounts.apps.AccountsConfig',
    'apps.blog',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 add this
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "core/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'blog_db',
#         'USER': 'blog_user',
#         'PASSWORD': 'strongpassword123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='postgresql://udoy_db_user:2zAC9Nlz9zm6LI541AHgOG32oG27pPCx@dpg-d774vp15pdvs73ceauf0-a.oregon-postgres.render.com/udoy_db')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / 'core/static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.user' # for custom user

# SMTP server setup 
# Email configuration setup 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'mdudoy00000@gmail.com'
EMAIL_HOST_PASSWORD= 'ihrmbziwqgjzosba'
DEFAULT_FROM_EMAIL= EMAIL_HOST_USER

JAZZMIN_SETTINGS = {
    "site_title": "UdoyBlog Admin",
    "site_header": "Udoy Dashboard",
    "site_brand": "UdoyBlog",
    "welcome_sign": "Welcome to your control panel 🚀",

    "topmenu_links": [
        {"name": "Home", "url": "list"},
        {"name": "Dashboard", "url": "user_dash"},
    ],

    "icons": {
        "blog.Blog": "fas fa-blog",
        "auth.User": "fas fa-user",
    },

    "theme": "darkly",  # 🔥 try: darkly, cyborg, flatly
}