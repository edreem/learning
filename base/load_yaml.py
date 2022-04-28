import os
import yaml


def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml",mode="r",encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]


def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",mode="a",encoding="utf-8") as f:
        yaml.dump(data,stream=f,allow_unicode=True)


def clear_yaml():
    with open(os.getcwd()+"/extract.yaml",mode="w",encoding="utf-8") as f:
        f.truncate()


def read_all(file_name):
    with open(os.getcwd()+"/data/"+file_name,mode="r",encoding="utf-8") as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value