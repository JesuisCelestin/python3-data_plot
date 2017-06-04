__author__ = 'Administrator'
#! /usr/bin/python<br> # -*- coding:utf8 -*-

from die import Die
import pygal
#创建一个骰子
die = Die()
#掷几次骰子， 并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
#分析结果
frequences = []
for value in range(1,die.num_sides+1):
    frequence = results.count(value)
    frequences.append(frequence)
#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = 'Results'
hist.y_title = 'Frequence of Result'
hist.add('D6', frequences)
hist.render_to_file('die_visual.svg')