import logging


# Set logging configuration. The default logging level is WARNING. By default, logs are sent to stdout.
# Again, unlike the root logger, a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(app_name)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename="logs/myapp.log")
# BasicConfig() can only be called once! 

# All logging functions can be called directly from the module. But it is good practice to create loggers 
# (This will make things easier as your app grows)
logger_name = __name__ if __name__ != "__main__" else "example_logger"
logger = logging.getLogger(logger_name)

# Configuring the logger with Handlers and Formatters
# Create handlers
c_handler = logging.StreamHandler()  # outputs to console
f_handler = logging.FileHandler('logs/error_file.log')  # outputs to a file
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
# Two handlers have been configured:
#   One that handles Warnings (and above) and outputs to the console. (Everything but DEBUG messages will be logged to the console)
#   One that handles Errors (and above) and outputs to a file. (ERROR & CRITICAL messages will be logged to the file)
# Everything is still logged to the file configured in basicConfig()

# extra args for the logs
app_name = "myapp"
extra_dict = {"app_name": app_name}

# Each level follows a hierarchical structure. If the level is INFO, all events at level INFO or higher will be logged.
logger.debug('This is a debug message', extra=extra_dict)
logger.info('This is an info message', extra=extra_dict)
logger.warning('This is a warning message', extra=extra_dict)
logger.error('This is an error message', extra=extra_dict)
logger.critical('This is a critical message', extra=extra_dict)

# Failure simulation, and trace capture.
str_a = "Hello"
str_b = "This will fail"

try:
    str_a / str_b
except Exception as e:
    # Capture trace with exc_info=True
    # logging.error(e, exc_info=True, extra=extra_dict)
    # using the exception method is the same as calling error(... , exc_info=True)
    logger.exception(e, extra=extra_dict)
