__author__ = 'Administrator'
#！ /usr/bin/python <br> #-*- coding:utf8 -*-
from random import randint

class Die():
    """表示一个骰子的类"""
    def __init__(self,num_sizes =6):
        self.num_sides = num_sizes

    def roll(self):
        """返回一个位于1和骰子面数之间的随机整数"""
        return randint(1,self.num_sides)
