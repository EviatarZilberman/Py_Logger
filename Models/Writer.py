import os
from datetime import datetime
from pathlib import Path
from Enums.LogLevels import LogLevel


class Writer(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, path, file_name):
        self._base_path = path
        file_path = Path(path)
        if file_path.exists():
            self._action = 'a'
        else:
            os.makedirs(path, exist_ok=True)
            self._action = 'w'
        self._file_name = file_name

    def write_log(self, data, level = LogLevel.INFO, file_name = None):
        log_level = level.value
        file_path = os.path.join(self._base_path, file_name or self._file_name)
        with open(file_path, self._action) as file:
            file.write(f'[{datetime.now()}] | [{log_level}] - {data}\n')



