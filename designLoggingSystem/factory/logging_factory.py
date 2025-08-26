from models import ErrorLogging, WarningLogging, InfoLogging, CriticalLogging, DebugLogging, LogLevel, Logging
from  datetime import datetime
class LoggerFactory:

    @staticmethod
    def get_logger(level: LogLevel, log_file=None) -> Logging:
        if level == LogLevel.ERROR:
            return ErrorLogging(log_file, level)
        elif level == LogLevel.WARNING:
            return WarningLogging(log_file, level)
        elif level == LogLevel.INFO:
            return InfoLogging(log_file, level)
        elif level == LogLevel.DEBUG:
            return DebugLogging(log_file, level)
        elif level == LogLevel.CRITICAL:
            return CriticalLogging(log_file, level)
        else:
            raise ValueError(f"Unknown log level: {level}")




