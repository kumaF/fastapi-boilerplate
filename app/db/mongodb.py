import logging

from bson import ObjectId
from fastapi.exceptions import HTTPException
from pymongo.errors import PyMongoError
from pymongo import (
    MongoClient,
    ReturnDocument
)

from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR
)

from ..configs import (
    MONGO_DB_NAME,
    MONGO_PACKAGE_COLLECTION,
    TIMEZONE
)

logger = logging.getLogger('app_logger')


class MongoDB:
    def __init__(self, client: MongoClient):
        self._client: MongoClient = client
        self._db = None
        self._tz = TIMEZONE
        self._package_coll = None

        try:
            self._client.server_info()
            self._db = self._client[MONGO_DB_NAME]
            self._package_coll = self._db[MONGO_PACKAGE_COLLECTION]
        except PyMongoError as e:
            logger.error(f'Database Connection Error ::: {str(e)}')

    def db_health_check(self):
        try:
            self._client.server_info()
            return True
        except PyMongoError as e:
            logger.error(f'[ mongodb.py > db_health_check ] ::: {str(e)}')
            return False

    