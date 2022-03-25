from .db import (
    open_db_connection,
    close_db_connection
)


def startup_handler():
    open_db_connection()


def shutdown_handler():
    close_db_connection()
