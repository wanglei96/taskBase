#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: 英雄工厂
 * @date: 2021/6/19
 * @version: 1.0
 * @fileName: hero_factory.py
 * @author: 'WangLei'
"""

from class_2_1_task.hero import *


class HeroFactory(object):

    @staticmethod
    def create_hero(name):
        """
        创建英雄
        :param name: 英雄名
        :return:
        """
        # 英雄字典
        dict_hero = {
            'Timo': Timo,
            'Jinx': Jinx
        }
        # 根据英雄名获取英雄类
        hero_model = dict_hero.get(name)
        if hero_model:
            return hero_model()
        else:
            raise Exception('没有找到英雄，请先创建英雄类')


if __name__ == "__main__":
    hero_timo = HeroFactory.create_hero('Timo')
    hero_jinx = HeroFactory.create_hero('Jinx')
    hero_timo.fight(hero_jinx.hp, hero_jinx.power)



