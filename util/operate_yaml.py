from rootpath import rootpath
import yaml
import os


# 获取当前脚本的所在文件夹的路径


def getData(yamlpath, node1, node2):
    with open(yamlpath, mode="r", encoding="utf-8") as f:
        # 用load方法将结果转成字典
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result[node1][node2]


# 已追加的方式写入yaml文件
def write_yaml(yamlpath, data):
    with open(yamlpath, mode="a", encoding="utf-8") as f:
        yaml.dump(data=data, stream=f, allow_unicode=True)

    # 读取extract.yaml中的配置信息


def get_extract(key):
    yamlpath = os.path.join(rootpath, "config/extract.yaml")
    with open(yamlpath, mode="r", encoding="utf-8") as f:
        result = yaml.load(stream=f, Loader=yaml.FullLoader)
        return result[key]

    # 读取caseinfo文件


def read_case_yaml(yamlpath):
    with open(yamlpath, mode="r", encoding="utf-8") as f:
        caseinfo = yaml.load(stream=f, Loader=yaml.FullLoader)
        return caseinfo[0]


# w' 以写入的方式打开文件，会覆盖已存在的文件,保持每次进行接口测试时的数据都是最
def clean_yaml(yamlpath):
    with open(yamlpath, mode="w") as f:
        f.truncate()


if __name__ == "__main__":
    read_case_yaml("../test_data/seal_list.yaml")
