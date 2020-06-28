# !/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/6/28 下午3:57
# @Author: Jtyoui@qq.com
# @Notes : 增加电话号码提取
import os
import re
import zipfile

from .phoneRegularity import chinese, PhoneRE
from .singleton import singletons


@singletons
class Phone:
    def __init__(self):
        self.file = os.path.join(os.path.dirname(__file__), 'telephone.zip')
        self.ds = {}
        data = self._extractfile()
        self._phone_map(data)

    def _extractfile(self):
        """读取zip压缩数据文本"""
        with zipfile.ZipFile(self.file)as zp:
            z = zp.read(zp.namelist()[0])
            data = z.decode('utf-8').split()
        return data

    def _phone_map(self, data: list):
        """电话前7位作为key，地址作为value"""
        for ls in data[1:]:
            values = ls.split(',')
            last = '0' + values[-1]
            self.ds[values[0]] = values[1:-1]
            self.ds[last] = values[1:-1]

    def extract(self, message: str):
        """抽取信息"""
        messages = []
        data = '@' + message.translate(chinese) + '@'  # 将口语化给替换成阿拉伯数字
        for k, v in PhoneRE.__dict__.items():
            if k.endswith('RE'):
                re_, type_ = v
                province, city, operators = '', '', ''
                match = re.finditer(re_, data)
                for m in match:
                    group = m.group()
                    index = data.find(group)
                    # 判断该数字前后都没有数字
                    if index > 0 and (not data[index - 1].isdigit()) and (not data[len(group) + index].isdigit()):
                        if '固定电话' == type_:
                            if len(group.replace('-', '')) == 11:
                                number = 3
                            elif len(group.replace('-', '')) == 12:
                                number = 4
                            else:
                                number = 5  # 香港
                        else:
                            number = 7
                        seven = group[:number]
                        message = self.ds.get(seven, None)
                        if message is not None:
                            province, city, operators = message
                        messages.append(
                            {'type': type_, 'province': province, 'city': city, 'operators': operators, 'value': group})
        return messages
