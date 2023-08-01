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

def FindFile_RenameCopy(file_name_list, src_all_path, output_path, out_file_name):
    file_path_list = []
    if(file_name_list == None):
        pass
    else :
        for file_name in file_name_list:
            for path in src_all_path:
                cur_filelist_path = FindFile(path, file_name)
                file_path_list += cur_filelist_path
                for cur_file_path in cur_filelist_path:
                    print(cur_file_path)
                    RenameCopyFile(cur_file_path, output_path, out_file_name)
    if(len(file_path_list) > 0):
        print(file_path_list)