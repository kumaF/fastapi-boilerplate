from uvicorn.logging import DefaultFormatter

LOG_LEVEL: str = 'DEBUG'
FORMAT: str = '%(levelprefix)s %(asctime)s - %(message)s'
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    'handlers': {
        'console': {
            'formatter': 'basic',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
            'level': LOG_LEVEL,
        }
    },
    'loggers': {
        'app_logger': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        }
    },
}