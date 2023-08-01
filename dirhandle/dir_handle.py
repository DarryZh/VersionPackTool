import os
import shutil
import glob

def FindFile(dir, suffix):
    return glob.glob(os.path.join(dir, suffix))

def RenameCopyFile(srcfile_path, target_path, new_name):
    (path, filename) = os.path.split(srcfile_path)
    (file, ext) = os.path.splitext(filename)
    new_file_path = os.path.join(target_path, new_name+ext)
    shutil.copyfile(srcfile_path,new_file_path)