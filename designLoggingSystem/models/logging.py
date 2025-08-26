import sys
from datetime import datetime
from .log_levels import LogLevel
from abc import ABC, abstractmethod

class Logging(ABC):
    def __init__(self, log_file=None):
        if log_file is None:
            self.log_file = self.get_log_filename()
        else:
            self.log_file = log_file

    @staticmethod
    def get_log_filename():
        now = datetime.now()
        # Rotate daily
        filename = f"log_{now.strftime('%Y-%m-%d')}.log"
        return filename

    def _get_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, level: LogLevel, message: str):
        timestamp = self._get_time()


        sys.stderr.write( f"{timestamp} {level.color}{level.label}{LogLevel.RESET.color}: {message}"+ "\n")
        sys.stderr.flush()


        with open(self.log_file, "a") as f:
            f.write(f"{timestamp} {level.label}: {message}\n")

    @abstractmethod
    def log(self, message: str):
        pass



class ErrorLogging(Logging):
    def __init__(self, log_file, level: LogLevel):
        super().__init__(log_file)
        self._level = level

    def log(self, message: str):
        self._write(self._level , message)


class WarningLogging(Logging):
    def __init__(self, log_file , level: LogLevel):
        super().__init__(log_file)
        self._level = level

    def log(self, message: str):
        self._write(self._level , message)



class InfoLogging(Logging):
    def __init__(self, log_file , level: LogLevel):
        super().__init__(log_file)
        self._level = level

    def log(self, message: str):
        self._write(self._level , message)



class DebugLogging(Logging):
    def __init__(self, log_file , level: LogLevel):
        super().__init__(log_file)
        self._level = level

    def log(self, message: str):
        self._write(self._level , message)



class CriticalLogging(Logging):
    def __init__(self, log_file , level: LogLevel):
        super().__init__(log_file)
        self._level = level

    def log(self, message: str):
        self._write(self._level , message)









