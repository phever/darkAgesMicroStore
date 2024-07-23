from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h70w6^6b#7w9uaql8umhkm#@uj2113^kut(l*ke!&-g3ck)uxw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Website url(s)
ALLOWED_HOSTS = ['*']

# FULL website url(s)
CSRF_TRUSTED_ORIGINS = ['http://*', 'https://*']

# Page Title/Header
STORE_TITLE = 'Phever.Shop'

# Remove 'made by phever'
MADE_BY = True

# Contact Info
YOUR_NAME = 'Phever'
DISCORD_HANDLE = 'Phever'

# Google Font, changes require CSS additions!
TITLE_FONT = 'Permanent Marker'
