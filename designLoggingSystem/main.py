from models import LogLevel
from factory import LoggerFactory

def main():
    error = LoggerFactory.get_logger(LogLevel.ERROR)
    critical = LoggerFactory.get_logger(LogLevel.CRITICAL)
    warning = LoggerFactory.get_logger(LogLevel.WARNING)
    info = LoggerFactory.get_logger(LogLevel.INFO)
    debug = LoggerFactory.get_logger(LogLevel.DEBUG)

    error.log("Syntax Error")
    critical.log("That system code is break")
    warning.log("It might be no longer")
    info.log("All is set")
    debug.log("Number done good")

    print(delete)


if __name__ == '__main__':
    main()