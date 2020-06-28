#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/8/9 9:56
# @Author: Jtyoui@qq.com
# @Notes : 一组匹配中国大陆手机号码的正则表达式。
chinese = {
    ord('一'): '1',
    ord('二'): '2',
    ord('三'): '3',
    ord('四'): '4',
    ord('五'): '5',
    ord('六'): '6',
    ord('七'): '7',
    ord('八'): '8',
    ord('九'): '9',
    ord('幺'): '1',
    ord('拐'): '7',
    ord('洞'): '0',
    ord('两'): '2',
    ord('勾'): '9'
}


class PhoneRE:
    # 移动手机卡
    MOVE_Card_RE = r'(?=<+86)?1(3[4-9]|5[0-27-9]|8[2378]|47)\d{8}', '移动手机卡'

    # 联通手机卡
    UNICOM_Card_RE = r'(?=<+86)?1(3[0126]|8[56]|66|45|5[56])\d{8}', '联通手机卡'

    # 电信手机卡
    TELECOM_Card_RE = r'(?=<+86)?1(3(3\d|49)\d|53\d{2}|8[019]\d{2}|7([37]\d{2}|40[0-5])|9[19]\d{2})\d{6}', '电信手机卡'

    # 匹配北京船舶通信导航有限公司（海事卫星通信）
    Maritime_Communications_RE = r'(?=<+86)?1749\d{7}', '海事卫星通信'

    # 工业和信息化部应急通信保障中心（应急通信）
    Emergency_Communication_RE = r'(?=<+86)?174(0[6-9]|1[0-2])\d{6}', '工业和信息化部应急通信保障中心'

    # 移动虚拟运营商
    Move_Virtual_Operator_RE = r'(?=<+86)?1(65\d|70[356])\d{7}', '移动虚拟运营商'

    # 联通虚拟运营商
    UNICOM_Virtual_Operator_RE = r'(?=<+86)?1(70[4789]|71\d|67\d)\d{7}', '联通虚拟运营商'

    # 电信虚拟运营商
    TELECOM_Virtual_Operator_RE = r'(?=<+86)?170[0-2]\d{7}', '电信虚拟运营商'

    # 移动物联网数据卡
    Move_Internet_of_Things_Data_Card_RE = r'(?=<+86)?14(40|8\d)\d{9}', '移动物联网数据卡'

    # 联通物联网数据卡
    UNICOM_Internet_of_Things_Data_Card_RE = r'(?=<+86)?146\d{10}', '联通物联网数据卡'

    # 电信物联网数据卡
    TELECOM_Internet_of_Things_Data_Card_RE = r'(?=<+86)?1410\d{9}', '电信物联网数据卡'

    # 移动上网卡
    MOVE_Wireless_Network_Card_RE = r'(?=<+86)?147\d{8}', '移动上网卡'

    # 联通上网卡
    UNiCOM_Wireless_Network_Card_RE = r'(?=<+86)?145\d{8}', '联通上网卡'

    # 电信上网卡
    TELECOM_Wireless_Network_Card_RE = r'(?=<+86)?149\d{8}', '电信上网卡'

    # 固定电话
    FIXED_TELEPHONE_RE = '0[0-9]{2,3}-?[0-9]{8}', '固定电话'
