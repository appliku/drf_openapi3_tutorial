import os
from configurations import values
from pathlib import Path
from speedpycom.settings import BaseConfig

# Temporary solution to make sure Django picks up the default auto_field.
# Model checks are performed before django-configurations are instantiated
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


class ProjectConfig(BaseConfig):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
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
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    PROJECT_APPS = [
        'usermodel',
        'main',
        'theme',
        'django_browser_reload',
        'blog',
    ]
    MIDDLEWARE = BaseConfig.MIDDLEWARE + [
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]

    SPECTACULAR_SETTINGS = {
        'TITLE': 'SpeedPyCom API',
        'DESCRIPTION': 'API documentation for SpeedPyCom based app',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
        # OTHER SETTINGS
    }

    WAGTAIL_SITE_NAME = 'SpeedPyCom'
    WAGTAILADMIN_BASE_URL = '/'
    SOCIALACCOUNT_GOOGLE_CLIENT_ID = values.Value()
    SOCIALACCOUNT_GOOGLE_CLIENT_SECRET = values.Value()

    @property
    def SOCIALACCOUNT_PROVIDERS(self):
        return {
            'google': {
                'SCOPE': [
                    'profile',
                    'email',
                ],
                # For each OAuth based provider, either add a ``SocialApp``
                # (``socialaccount`` app) containing the required client
                # credentials, or list them here:
                'APP': {
                    'client_id': self.SOCIALACCOUNT_GOOGLE_CLIENT_ID,
                    'secret': self.SOCIALACCOUNT_GOOGLE_CLIENT_SECRET,
                    'key': ''
                }
            }
        }
