import re
import pyyaml.lib.yaml as yaml

def ParseYaml(yaml_file):
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    
    data = list(yaml.load_all(file_data, Loader=yaml.FullLoader))
    return data

class ParseProject(object):
    def __init__(self, project:dict):
        self.project = project
        if('PROJECT' in project.keys()):
            self.prefix = ''
        elif('SUB1_PROJECT' in project.keys()):
            self.prefix = 'SUB1_'
        elif('SUB2_PROJECT' in project.keys()):
            self.prefix = 'SUB2_'
        pass
    def get_project_name(self) -> str:
        if((self.project[self.prefix+'PROJECT']) == None):
            return None
            # raise Exception('project name type is not string')
        for name in self.project[self.prefix+'PROJECT']:
            return name
    def get_path(self) -> list:
        if((self.project[self.prefix+'SEARCH_PATH']) == None):
            return None
        return self.project[self.prefix+'SEARCH_PATH']
    def get_version_header_file(self) -> list:
        if((self.project[self.prefix+'VERSION_HEADER_FILE']) == None):
            return None
        for ver in self.project[self.prefix+'VERSION_HEADER_FILE']:
            return ver
    def get_version_re(self) -> list:
        if((self.project[self.prefix+'VERSION_RE']) == None):
            return None
        for ver_re in self.project[self.prefix+'VERSION_RE']:
            return ver_re
    def get_output_path(self) -> list:
        if((self.project[self.prefix+'OUTPUT_PATH']) == None):
            return None
        for ver in self.project[self.prefix+'OUTPUT_PATH']:
            return ver
    def get_bootloader(self) -> list:
        if((self.project[self.prefix+'BOOTLOADER']) == None):
            return None
        return self.project[self.prefix+'BOOTLOADER']
    def get_partition_table(self) -> list:
        if((self.project[self.prefix+'PARTITION_TABLE']) == None):
            return None
        return self.project[self.prefix+'PARTITION_TABLE']
    def get_kernel(self) -> list:
        if((self.project[self.prefix+'KERNEL']) == None):
            return None
        return self.project[self.prefix+'KERNEL']
    def get_fs(self) -> list:
        if((self.project[self.prefix+'FS']) == None):
            return None
        return self.project[self.prefix+'FS']
    def get_release(self) -> list:
        if((self.project[self.prefix+'RELEASE']) == None):
            return None
        return self.project[self.prefix+'RELEASE']
    def get_debug(self) -> list:
        if((self.project[self.prefix+'DEBUG']) == None):
            return None
        return self.project[self.prefix+'DEBUG']
    def get_ota(self) -> list:
        if((self.project[self.prefix+'OTA']) == None):
            return None
        return self.project[self.prefix+'OTA']

def parse_version_by_re(file_path:str, ver_re) -> str:
    data = ''
    with open(file_path, "r") as f: 
        data = f.read()  
        f.close()

    ret = re.findall(ver_re, data)

    for data in ret:
        return data