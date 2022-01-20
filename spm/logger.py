import logging


class SPMLogger(object):
    def __init__(self, logger_name, log_level):
        self.logger_name = logger_name
        self.log_level = log_level
        self.logger = self.get_logger(self.logger_name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        numeric_level = logging.getLevelName(log_level.upper())
        if not isinstance(numeric_level, int):
            raise ValueError("Invalid log level: %s" % log_level)
        self.logger.setLevel(numeric_level)

    @staticmethod
    def get_logger(logger_name):
        return logging.getLogger(logger_name)
