import os
import shutil
import glob
import zipfile

def FindFile(dir, suffix):
    return glob.glob(os.path.join(dir, suffix))

def RenameCopyFile(srcfile_path, target_path, new_name):
    (path, filename) = os.path.split(srcfile_path)
    (file, ext) = os.path.splitext(filename)
    new_file_path = os.path.join(target_path, new_name+ext)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
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
                    RenameCopyFile(cur_file_path, output_path, out_file_name)
    if(len(file_path_list) > 0):
        print(file_path_list)

def generate_zipfile(src_path, target_path, zipname):
    oldwd = os.getcwd()
    os.chdir(src_path)
    try:
        new_file_path = os.path.join(target_path, zipname+'.zip')
        #新建zip文件 使用写操作w也可以使用追加a
        myzip = zipfile.ZipFile(new_file_path,'w')
        print(os.walk('.'))
        for current_path,subfolders,filesname in os.walk('.'):
            #current_path 当前路径
            #subfolders 当前路径下的文件夹
            #filesname当前目录下的文件
            print(current_path,subfolders,filesname)
            for file in filesname:
                myzip.write(os.path.join(current_path,file), compress_type=zipfile.ZIP_LZMA)
    finally:
        os.chdir(oldwd)

    #关闭
    myzip.close()
