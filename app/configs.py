import os

from urllib.parse import quote_plus
from starlette.config import Config

config = Config('.env')

API_VERSION = config('API_VERSION', cast=str, default='v0.1')
API_PREFIX = f'/api/{API_VERSION}'
TIMEZONE = config('TIMEZONE', cast=str, default='UTC')

MONGO_HOST = config('MONGO_HOST', cast=str, default='localhost')
MONGO_PORT = config('MONGO_PORT', cast=str, default='27017')
MONGO_DB_NAME = config('MONGO_DB_NAME', cast=str, default='auth_db')
MONGO_USERNAME = config('MONGO_USERNAME', cast=str, default='admin')
MONGO_PASSWORD = config('MONGO_PASSWORD', cast=str, default='Kyco@mongo123')

MONGO_TIMEOUT = 3000
MONGO_URL = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'

# MONGO_URL = f'mongodb://{quote_plus(MONGO_USERNAME)}:{quote_plus(MONGO_PASSWORD)}@{MONGO_HOST}:{MONGO_PORT}'

MONGO_PACKAGE_COLLECTION = config('MONGO_PACKAGE_COLLECTION', cast=str, default='packages_collection')
