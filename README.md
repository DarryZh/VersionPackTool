VersionPackTool
======

仅依赖原生python（无pip包依赖），跨平台（linux windows），支持子工程，可配置的软件打包工具，自动生成所指定规则

## 环境

Python （已验证 3.11.4）

## 使用
 - 克隆并 git submodule update --init --recursive
 - 使用default_config.yaml模板，创建用户工程config.yaml
 - 配置config.yaml必要选项，详情见“配置文件说明”
 - 运行 python execute.py

## yaml配置文件说明

    PROJECT:        #主工程名
    - F10

    SEARCH_PATH:    #资源搜索路径
    - D:\output

    VERSION_HEADER_FILE:    #版本号头文件文件名
    - __version__.h

    VERSION_RE:             #版本号头文件中版本号的正则表达式
    - '\d.\d.\d.\d'
    
    OUTPUT_PATH:            #产物输出目录
    - D:\output

    BOOTLOADER:             #bootloader 
    - '*.bin'

    PARTITION_TABLE:        #分区表
    - '*.bin'

    KERNEL:                 #kernel
    - '*.bin'

    FS:                     #文件系统
    - '*.bin'

    RELEASE:                #发布版本
    - '*.bin'
    - '*.hex'

    DEBUG:                  #调试版本
    - '*.axf'
    - '*.elf'
    - '*.map'

    OTA:                    #ota文件
    - '*.bin'

    # sub project 1           #子项目1，同上
    ---
    SUB1_PROJECT:

    SUB1_SEARCH_PATH:

    SUB1_VERSION_HEADER_FILE:

    SUB1_OUTPUT_PATH:

    SUB1_BOOTLOADER:

    SUB1_PARTITION_TABLE:

    SUB1_KERNEL:

    SUB1_FS:

    SUB1_RELEASE:

    SUB1_DEBUG:

    SUB1_OTA:

    # sub project 2           #子项目2，同上
    ...
