from datetime import datetime
from pathlib import Path

from Enums.LogLevels import LogLevel


class Writer(object):
    _m_instance = None
    _m_base_path = None
    _m_file_name = None
    _m_action = 'w'

    def __new__(cls, *args, **kwargs):
        if not cls._m_instance:
            cls._m_instance = super().__new__(cls)
        return cls._m_instance

    def __init__(self, path, file_name):
        self._m_base_path = path
        file_path = Path(path)
        if file_path.exists():
            self._m_action = 'a'
        self._m_file_name = file_name

    def write_log(self, data, level = 'i', file_name = None):
        log_level = Writer._get_log_level(level)
        if file_name:
            new_path = f'{self._m_base_path}\\{file_name}'
        else:
            new_path = f'{self._m_base_path}\\{self._m_file_name}'
        file = open(new_path, self._m_action)
        file.write(f'[{datetime.now()}] | [{log_level}] - {data}\n')
        pass

    @staticmethod
    def _get_log_level(level) -> str:
        if level == 'i':
            return str(LogLevel.i.value)
        elif level == 'e':
            return str(LogLevel.e.value)
        elif level == 'f':
            return str(LogLevel.f.value)
        else:
            return 'Invalid log level!'

