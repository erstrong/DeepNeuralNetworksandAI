import logging
import os

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class Logger:
    __shared_state = {}
    logger = None

    default_level = logging.INFO
    default_path = "../../../logs/"
    default_name = "app.log"

    def __init__(self, level=None):
        self.__dict__ = self.__shared_state
        self.set_level(level)

    def set_path(self, path):
        self.default_path = path
        return self

    def set_level(self, level):
        self.default_level = LEVELS.get(level, self.default_level)
        logging.basicConfig(level=self.default_level)
        return self

    def get_logger(self, name=None):
        if name is None:
            if self.logger is not None:
                return self.logger
            name = self.default_name
        else:
            name = name + ".log"

        new_logger = logging.getLogger(name)

        if not os.path.isdir(self.default_path):
            os.makedirs(self.default_path)
        file_handle = logging.FileHandler(os.path.join(self.default_path, name), 'w')
        file_handle.setLevel(self.default_level)
        new_logger.addHandler(file_handle)

        stream_handle = logging.StreamHandler()
        stream_handle.setLevel(self.default_level)
        new_logger.addHandler(stream_handle)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handle.setFormatter(formatter)
        stream_handle.setFormatter(formatter)

        new_logger.propagate = False

        if name == self.default_name:
            self.logger = new_logger
        return new_logger
