from enum import Enum

class LogLevel(Enum):
    DEBUG   = ("DEBUG", "\033[94m")   # Blue
    INFO    = ("INFO", "\033[92m")    # Green
    WARNING = ("WARNING", "\033[93m") # Yellow
    ERROR   = ("ERROR", "\033[91m")   # Red
    CRITICAL= ("CRITICAL", "\033[95m")# Magenta
    RESET   = ("RESET", "\033[37m")    # Reset color

    @property
    def label(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]