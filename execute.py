import os
import configparse.config_parse as ConfigParse
import dirhandle.dir_handle as DirHandle

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "config.yaml")

config = ConfigParse.ParseYaml(yaml_path)

print('project cnt is :' + str(len(config)))

combine_name = ''
all_path = ''
output_path = ''

for cfg in config:
    ParsePro = ConfigParse.ParseProject(cfg)
    project_name = ''

    if('PROJECT' in cfg.keys()):
        project_name = ParsePro.get_project_name()
        combine_name += ParsePro.get_project_name()
    if('SEARCH_PATH' in cfg.keys()):
        all_path = ParsePro.get_path()
    if('VERSION_HEADER_FILE' in cfg.keys()):
        print(ParsePro.get_version_header_file())
    if('OUTPUT_PATH' in cfg.keys()):
        output_path = ParsePro.get_output_path()
    if('BOOTLOADER' in cfg.keys()):
        file_name_list = ParsePro.get_bootloader()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'BootLoarder_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('PARTITION_TABLE' in cfg.keys()):
        file_name_list = ParsePro.get_partition_table()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'PartitonTable_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('KERNEL' in cfg.keys()):
        file_name_list = ParsePro.get_kernel()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'Kernel_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('FS' in cfg.keys()):
        file_name_list = ParsePro.get_fs()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'FS_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('RELEASE' in cfg.keys()):
        file_name_list = ParsePro.get_release()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'Release_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('DEBUG' in cfg.keys()):
        file_name_list = ParsePro.get_debug()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'Debug_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)
    if('OTA' in cfg.keys()):
        file_name_list = ParsePro.get_ota()
        file_path_list = []
        if(file_name_list == None):
            pass
        else :
            for file_name in file_name_list:
                for path in all_path:
                    cur_filelist_path = DirHandle.FindFile(path, file_name)
                    file_path_list += cur_filelist_path
                    print(cur_filelist_path)
                    for cur_file_path in cur_filelist_path:
                        DirHandle.RenameCopyFile(cur_file_path, output_path, 'OTA_' + project_name)
        if(len(file_path_list) > 0):
            print(file_path_list)

print('project name : ' + combine_name)
