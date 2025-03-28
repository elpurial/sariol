"""
Django settings for datos_clientes project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'datos_clientes.settings'
import dj_database_url
from decouple import config



RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [ 
   
    ]
RENDER_EXTERNAL_HOSTNAME=config('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tools',
    'servicios',
    'blog',
    'tienda',   
    'contacto',
    'widget_tweaks',
    'gmails',
    'carro', 
    'autenticacion', 
    'crispy_forms',
    'crispy_bootstrap5', 
    'pedidos', 
    'reservas', 
    'django_seed',
    'uno_a_uno',
    'uno_a_muchos',  
    'solicitudes',
    
    
        
]
from django.contrib.messages import constants as mensajes_de_error

MESSAGE_LEVEL = mensajes_de_error.DEBUG

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'datos_clientes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(RUTA_PROYECTO,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro'
            ],
        },
    },
]

WSGI_APPLICATION = 'datos_clientes.wsgi.application'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":config('DB_NAME'),
        "USER":config('DB_USER'),
        "PASSWORD":config('DB_PASSWORD'),
        "HOST":config('DB_HOST'),
        "PORT": config('DB_PORT',cast=int)
       
        
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Havana'

USE_I18N = True
USE_TZ = True
#USE_TZ = False

DATE_INPUT_FORMATS = ['%d-%m-%Y']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Directories to search for static files
STATICFILES_DIRS = [
    os.path.join(RUTA_PROYECTO, "static"),
]

MEDIA_ROOT =  os.path.join(RUTA_PROYECTO, "media")
MEDIA_URL = "/media/"



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CONFIGURACION DEL CORREO ELECTRONICO
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT',cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')   # PASSWORD GENERADA EN GMAIL PARA ESTE CORREO (TENGO QUE HACERLO DESDE LA PROPIA CUENTA QUE PUSE ARRIBA)
EMAIL_USE_TLS = True





MESSAGE_TAGS = {
    
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.DEBUG:'debug',
    mensajes_de_error.SUCCESS: 'success',
    mensajes_de_error.WARNING:'warning',
    mensajes_de_error.ERROR:'danger',    
    
    
}
