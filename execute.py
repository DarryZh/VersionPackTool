import os
import shutil
import configparse.config_parse as ConfigParse
import dirhandle.dir_handle as DirHandle


CONFIG_YAML_NAME = 'config.yaml'

BOOTLOADER_PREFIX = 'BL_'
PARTITION_TABLE_PREFIX = 'PartitonTable_'
KERNEL_PREFIX = 'Kernel_'
FS_PREFIX = 'FS_'
RELEASE_PREFIX = 'Release_'
DEBUG_PREFIX = 'Debug_'
OTA_PREFIX = 'OTA_'

combine_name = ''
output_path = ''
tmp_output_path = ''

if __name__ == '__main__':
    current_path = os.path.abspath(".")
    yaml_path = os.path.join(current_path, CONFIG_YAML_NAME)

    config = ConfigParse.ParseYaml(yaml_path)
    project_cnt = len(config)
    print('project cnt is :' + str(project_cnt))

    for cfg in config:
        all_path = ''
        project_name = ''
        project_name_version = ''
        version_header_file_path = ''
        project_version = ''

        tmp_release_output_path = ''
        tmp_ota_output_path = ''
        tmp_debug_output_path = ''

        ParsePro = ConfigParse.ParseProject(cfg)

        # if('PROJECT' in cfg.keys()):
        project_name = ParsePro.get_project_name()
        if project_name != None:
            if(combine_name != ''):
                combine_name += '_'
            combine_name += ParsePro.get_project_name()
        # if('SEARCH_PATH' in cfg.keys()):
        all_path = ParsePro.get_path()
        # if('VERSION_HEADER_FILE' in cfg.keys()):
        file_name = ParsePro.get_version_header_file()
        if(file_name != None):
            for path in all_path:
                cur_filelist_path = DirHandle.FindFile(path, file_name)
                for cur_file_path in cur_filelist_path:
                    print(cur_file_path)
                    version_header_file_path = cur_file_path
        # if('VERSION_RE' in cfg.keys()):
        version_re = ParsePro.get_version_re()
        if version_re != None:
            project_version = ConfigParse.parse_version_by_re(version_header_file_path, version_re)
            combine_name += '_v' + project_version
            project_name_version = project_name + '_v' + project_version
        if('OUTPUT_PATH' in cfg.keys()):
            output_path = ParsePro.get_output_path()
        if output_path != None:
            tmp_output_path = os.path.join(output_path, 'tmp')
            if(project_cnt > 1):
                tmp_release_output_path = os.path.join(output_path, 'tmp', 'release', project_name)
                tmp_ota_output_path = os.path.join(output_path, 'tmp', 'ota', project_name)
                tmp_debug_output_path = os.path.join(output_path, 'tmp', 'debug', project_name)
            else:
                tmp_release_output_path = os.path.join(output_path, 'tmp', 'release')
                tmp_ota_output_path = os.path.join(output_path, 'tmp', 'ota')
                tmp_debug_output_path = os.path.join(output_path, 'tmp', 'debug')
        # if('BOOTLOADER' in cfg.keys()):
        file_name_list = ParsePro.get_bootloader()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_release_output_path, BOOTLOADER_PREFIX+project_name_version)
        # if('PARTITION_TABLE' in cfg.keys()):
        file_name_list = ParsePro.get_partition_table()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_release_output_path, PARTITION_TABLE_PREFIX+project_name_version)
        # if('KERNEL' in cfg.keys()):
        file_name_list = ParsePro.get_kernel()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_release_output_path, KERNEL_PREFIX+project_name_version)
        # if('FS' in cfg.keys()):
        file_name_list = ParsePro.get_fs()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_release_output_path, FS_PREFIX+project_name_version)
        # if('RELEASE' in cfg.keys()):
        file_name_list = ParsePro.get_release()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_release_output_path, RELEASE_PREFIX+project_name_version)
        # if('DEBUG' in cfg.keys()):
        file_name_list = ParsePro.get_debug()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_debug_output_path, DEBUG_PREFIX+project_name_version)
        # if('OTA' in cfg.keys()):
        file_name_list = ParsePro.get_ota()
        if file_name_list != None:
            DirHandle.FindFile_RenameCopy(file_name_list, all_path, tmp_ota_output_path, OTA_PREFIX+project_name_version)

    print('project name : ' + combine_name)
    if output_path != None and combine_name != '':
        DirHandle.generate_zipfile(tmp_output_path, output_path, combine_name)
    shutil.rmtree(tmp_output_path) 