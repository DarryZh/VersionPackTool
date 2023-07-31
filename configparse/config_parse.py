import os
import sys
import pyyaml.lib.yaml as yaml

def ParseYaml(yaml_file):
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    
    data = yaml.load_all(file_data, Loader=yaml.FullLoader)
    # for project in data:
    #     print(project)
    return data