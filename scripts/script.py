import pandas as pd
import numpy as np
import os
import json


def mylen(x):
    if isinstance(x, float):
        return 0
    else:
        return len(x)

def getlen(row):
    return pd.Series({
        'label': mylen(row['LABEL']),
        'brand': mylen(row['品牌']),
        'nickname': mylen(row['别名']),
        'origin': mylen(row['产地']),
        'company': mylen(row['隶属公司']),
        'createtime': mylen(row['成立时间']),
        'cofounder': mylen(row['创始人']),
        'site': mylen(row['官网']),
        'about': mylen(row['简介']),
    })

def generate_label2index(dir):
    name2label = {}
    for subdir in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, subdir)):
            name2label[subdir] = len(name2label)
    return name2label



