#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: **
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: config_data.py
 * @author: 'WangLei'
"""
import yaml

from class_5_2_task.utils.setting import LOGGER, DATA_DIR


def load_yaml(file_path):
    """
    读取yaml文件数据
    :param file_path: 文件路径
    :return:
    """
    LOGGER.info(f'加载yaml文件: {file_path}')
    # 读取yaml文件数据
    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


# print(load_yaml(DATA_DIR))