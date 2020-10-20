import os

topdir = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
appfolder = os.path.abspath(os.path.join(topdir, "app"))
logfolder = os.path.abspath(os.path.join(topdir, "logs"))
cachefolder = os.path.abspath(os.path.join(topdir, "cache"))
uploadfolder = os.path.abspath(os.path.join(topdir, "upload"))


# settings
LOG_MONITOR_ENABLE = False

# permissions & roles

class PERMISSIONS(object):
    P1 = 0b00000001 or 1
    P2 = 0b00000010 or 2
    P3 = 0b00000100 or 4
    P4 = 0b00001000 or 8
    P5 = 0b00010000 or 16
    P6 = 0b00100000 or 32
    P7 = 0b01000000 or 64
    P8 = 0b10000000 or 128

class ROLES(object):
    VIEW = PERMISSIONS.P1
    ADMIN = PERMISSIONS.P1+PERMISSIONS.P2
    SUPERADMIN = PERMISSIONS.P1+PERMISSIONS.P2+PERMISSIONS.P3
