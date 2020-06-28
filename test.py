#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/2/18 15:23
# @Author: Jtyoui@qq.com
from pyunit_phone import Phone

phone = Phone()


def check_up():
    data = """
    我的电话是15180865874,
    他的电话是0851-12456789,
    骚扰电话：075523675665,
    01051369070 18716521010 
    """
    assert phone.extract(data) == \
           [{
               'city': '贵阳',
               'operators': '移动',
               'province': '贵州',
               'type': '移动手机卡',
               'value': '15180865874'
           },
               {
                   'city': '万州',
                   'operators': '移动',
                   'province': '重庆',
                   'type': '移动手机卡',
                   'value': '18716521010'
               },
               {
                   'city': '贵阳',
                   'operators': '电信',
                   'province': '贵州',
                   'type': '固定电话',
                   'value': '0851-12456789'
               },
               {
                   'city': '深圳',
                   'operators': '电信',
                   'province': '广东',
                   'type': '固定电话',
                   'value': '075523675665'
               },
               {
                   'city': '北京',
                   'operators': '电信',
                   'province': '北京',
                   'type': '固定电话',
                   'value': '01051369070'
               }
           ]


if __name__ == '__main__':
    check_up()
