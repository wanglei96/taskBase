#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: 项目路径管理
 * @date: 2021/8/22
 * @version: 1.0
 * @fileName: setting.py
 * @author: 'WangLei'
"""
import logging
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 测试数据目录
DATA_DIR = str(BASE_DIR) + '/datas/data.yml'

# 日志配置
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger('AutoApiTest')


