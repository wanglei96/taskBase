#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: 计算器测试用例
 * @date: 2021/6/27
 * @version: 1.0
 * @fileName: test_calculator.py
 * @author: 'WangLei'
"""
import allure
import pytest
import yaml

# 读取测试数据
with open('../test_datas/cals.yaml', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)
    add_data = test_data['add']['datas']
    add_ids = test_data['add']['mid']
    div_data = test_data['div']['datas']
    div_ids = test_data['div']['mid']

@pytest.mark.parametrize('a, b, expect', add_data, ids=add_ids)
def test_add( a, b, expect, get_clac, logger):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # 计算结果，保留2位小数
        actual = round(get_clac.add(a, b), 2)
        logger.info(f"预期值：{expect}, 实际值：{actual}")
        # 断言
        assert actual == expect
    else:
        assert False, "参数类型必须为int 或 float"


@allure.feature("计算器测试")
class TestCalculator:

    @allure.story("测试加法")
    @pytest.mark.parametrize('a, b, expect', add_data, ids=add_ids)
    def test_add(self, a, b, expect, get_clac, logger):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # 计算结果，保留2位小数
            actual = round(get_clac.add(a, b), 2)
            logger.info(f"预期值：{expect}, 实际值：{actual}")
            # 断言
            assert actual == expect
        else:
            assert False, "参数类型必须为int 或 float"

    @allure.story("测试除法")
    @pytest.mark.parametrize('a, b, expect', div_data, ids=div_ids)
    def test_div(self, a, b, expect, get_clac, logger):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if b != 0:
                # 计算结果，保留2位小数
                actual = round(get_clac.div(a, b), 2)
                logger.info(f"预期值：{expect}, 实际值：{actual}")
                # 断言
                assert actual == expect
            else:
                assert False, "除数不能为0"
        else:
            assert False, "参数类型必须为int 或 float"
