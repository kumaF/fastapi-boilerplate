import logging

from pymongo import MongoClient

from ..configs import (
    MONGO_TIMEOUT,
    MONGO_URL
)

logger = logging.getLogger('app_logger')

class Database:
    client: MongoClient = None


db = Database()


def open_db_connection():
    logger.info('Establishing database connection')
    try:
        db.client = MongoClient(
            MONGO_URL,
            serverSelectionTimeoutMS=MONGO_TIMEOUT
        )

        db.client.server_info()
        logger.info('Connected to database successfully')
    except Exception as e:
        logger.error(f'Conecting to database failed ::: {e}')


def close_db_connection():
    logger.info('Closing database connection')
    try:
        db.client.close()
        logger.info('Database diconnected successfully')
    except:
        logger.error('Database diconnected failed')


def get_client() -> MongoClient:
    return db.client
