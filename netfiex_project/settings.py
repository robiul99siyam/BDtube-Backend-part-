

from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()




BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^*-%*4@&(kwe#$_q251ocywn)0v5n^-+ug7)y56gf5hkirqzx1'


DEBUG = True

ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ['.vercel.app','now.sh']

INSTALLED_APPS = [
    # "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "netfiex_app",
    "user_auth",
    'rest_framework.authtoken',
    # 'channels',
    "debug_toolbar",
   

    #Extranal 
    'corsheaders',
    'django_filters', 
]
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Moved cors middleware before common
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Ensure it's listed only once
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]



ROOT_URLCONF = 'netfiex_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'netfiex_project.wsgi.application'
# ASGI_APPLICATION = 'netfiex_project.asgi.application'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}





# CACHES = {
   
#     "default": {
        
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",

     
#         "LOCATION": "unique-snowflake",
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles_build'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]