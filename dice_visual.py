__author__ = 'Administrator'
#! /usr/bin/python<br> # -*- coding:utf8 -*-

from die import Die
import pygal
#创建一个骰子
die_1 = Die()
die_2 = Die()
#掷几次骰子， 并将结果储存在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
#分析结果
frequences = []
max_results = die_1.num_sides + die_2.num_sides
'''
for value in range(2,max_results+1):
    frequence = results.count(value)
    frequences.append(frequence)
'''
frequences = [results.count(value) for value in range(2,max_results+1)]
#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 dice 1000 times'
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = range(2,max_results+1)
hist.x_title = 'Results'
hist.y_title = 'Frequence of Result'
hist.add('D6+D6', frequences)
hist.render_to_file('dice_visual.svg')