import logging
from logging.handlers import RotatingFileHandler
import os

from  app.myglobals import logfolder


formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 1. logger property set up
logfile1 = os.path.abspath(os.path.join(logfolder, "log_module1.txt"))
logfile2 = os.path.abspath(os.path.join(logfolder, "log_module2.txt"))


# handler = logging.FileHandler(logfile)
filehandler1 = RotatingFileHandler(logfile1, maxBytes = 10*1024*1024, backupCount=10)
filehandler1.setLevel(logging.INFO)
filehandler1.setFormatter(formatter1)

filehandler2 = RotatingFileHandler(logfile2, maxBytes = 10*1024*1024, backupCount=3)
filehandler2.setLevel(logging.INFO)
filehandler2.setFormatter(formatter1)

consolehandler1 = logging.StreamHandler()
consolehandler1.setLevel(logging.INFO)
consolehandler1.setFormatter(formatter1)

consolehandler2 = logging.StreamHandler()
consolehandler2.setLevel(logging.INFO)
consolehandler2.setFormatter(formatter1)

# 2.1 logger init
logger_module1 = logging.getLogger('module1')
logger_module1.setLevel(level = logging.INFO)
logger_module1.addHandler(filehandler1)
logger_module1.addHandler(consolehandler1)

# 2.2 logger init
logger_module2 = logging.getLogger('module2')
logger_module2.setLevel(level = logging.INFO)
logger_module2.addHandler(filehandler2)
logger_module2.addHandler(consolehandler2)

