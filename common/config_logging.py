import logging
import logging.config
import os
from datetime import datetime
from erp_lib.config import settings

class LoggingConfig:
    """Configures logging for the application with various handlers."""

    def __init__(self, module_name='default', sqlalchemy_logger=False):
        """
        Initializes the LoggingConfig instance.

        Args:
            module_name (str): The name of the module for which to configure logging.
            sqlalchemy_logger (bool): Whether to add a logger for SQLAlchemy engine.
        """
        self.module_name = module_name
        self.sqlalchemy_logger = sqlalchemy_logger
        self.setup_logging()

    def setup_logging(self):
        """
        Sets up logging configuration based on settings and provided options.
        """
        log_level = settings.LOG_LEVEL.upper()
        log_file_folder = settings.LOG_FILE_FOLDER
        log_http_host = settings.LOG_HTTP_HOST
        log_http_url = settings.LOG_HTTP_URL

        # Ensure the log file folder exists
        if not os.path.exists(log_file_folder):
            os.makedirs(log_file_folder)

        # Generate a date-specific log file name
        current_date = datetime.now().strftime('%Y-%m-%d')
        log_file_name = f"application_{current_date}.log"
        log_file_path = os.path.join(log_file_folder, log_file_name)

        logging_config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'level': log_level,
                },
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': log_file_path,
                    'formatter': 'default',
                    'level': log_level,
                },
                'http': {
                    'class': 'logging.handlers.HTTPHandler',
                    'host': log_http_host,
                    'url': log_http_url,
                    'method': 'POST',
                    'formatter': 'default',
                },
            },
            'loggers': {
                '': {
                    'level': log_level,
                    'handlers': ['console', 'file', 'http'],
                },
                self.module_name: {
                    'level': log_level,
                    'handlers': ['console', 'file'],
                    'propagate': False,
                },
                'sqlalchemy.engine': {
                    'level': logging.INFO,
                    # 'handlers': ['console'],
                    'propagate': False,
                }
            },
        }

        try:
            logging.config.dictConfig(logging_config)
        except Exception as e:
            # Use logging instead of print
            logging.error(f"Error configuring logging: {e}")

    def get_logger(self):
        """
        Returns a logger instance configured for the given module.

        Returns:
            logging.Logger: The configured logger for the module.
        """
        return logging.getLogger(self.module_name)
