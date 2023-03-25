LOG_LEVEL: str = "INFO"
FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging_config = {
    "version": 1, # mandatory field
    # if you want to overwrite existing loggers' configs
    "disable_existing_loggers": False,
    "formatters": {
        "basic": {
            "format": FORMAT,
        }
    },
    "handlers": {
        "console": {
            "formatter": "basic",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        }
    },
    "loggers": {
        "pipeline": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "template": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        }
    },
}
