import xlwt
import os
import datetime
import shutil
import json

from app.myglobals import topdir, logfolder, appfolder

# please be very careful to call this function
def empty_folder(folder):
    files = os.listdir(folder)
    for file in files:
        if file == '.gitkeep':
            continue
        file = os.path.join(folder, file)
        # todo
        # if file type is folder, here will raise IsADirectoryError
        os.remove(file)

def empty_dir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # print('==root==', root)
        for name in files:
            # print('==file==', name)
            if name =='.gitkeep':
                continue
            os.remove(os.path.join(root, name))
        for name in dirs:
            # print('==dir==', name)
            # os.removedirs(os.path.join(root, name))
            os.rmdir(os.path.join(root, name))

def rm_pycache(path):
     for root, dirs, files in os.walk(path, topdown=False):
        for name in dirs:
            if name == '__pycache__':
                # os.removedirs(os.path.join(root, name))
                shutil.rmtree(os.path.join(root, name))

def write_json_to_file(o_dict, filename):
    with open(filename, 'w') as f:
        json.dump(o_dict, f, indent=4)


def cleanup_log():
    empty_dir(logfolder)

def cleanup_pycache():
    # rm_pycache(appfolder)
    rm_pycache(topdir)


