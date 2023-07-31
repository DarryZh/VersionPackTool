import os
import sys

import configparse.config_parse as ConfigParse

current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "config.yaml")

config = ConfigParse.ParseYaml(yaml_path)

print(len(config))

# for cfg in config:
