#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 * @description: 英雄类
 * @date: 2021/6/19
 * @version: 1.0
 * @fileName: hero.py
 * @author: 'WangLei'
"""


class Hero(object):
    hp = 0
    power = 0

    def fight(self, enemy_hp, enemy_power):
        """
        战斗方法
        :param enemy_hp: 敌人血量
        :param enemy_power: 敌人攻击力
        :return:
        """
        hero_finally_hp = self.hp - enemy_power
        enemy_finally_hp = enemy_hp - self.power
        if hero_finally_hp > enemy_finally_hp:
            print('英雄获胜')
        elif hero_finally_hp < enemy_finally_hp:
            print('敌人获胜')
        else:
            print('平局')


class Timo(Hero):
    hp = 1000
    power = 100


class Jinx(Hero):
    hp = 2000
    power = 100



