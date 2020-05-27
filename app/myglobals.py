import os

topdir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
appfolder = os.path.abspath(os.path.join(topdir, "app"))
logfolder = os.path.abspath(os.path.join(topdir, "log"))
cachefolder = os.path.abspath(os.path.join(topdir, "cache"))
uploadfolder = os.path.abspath(os.path.join(topdir, "upload"))


# settings
LOG_MONITOR_ENABLE = False
