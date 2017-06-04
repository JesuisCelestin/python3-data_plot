__author__ = 'Administrator'
#! /usr/bin/python<br> # -*- coding: utf8 -*-

from die import Die
import pygal
#创建一个骰子
die_1 = Die(num_sizes=8)
die_2 = Die(num_sizes=8)
#掷几次骰子， 并将结果储存在一个列表中

'''
results = []
for roll_num in range(10000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
'''
results = [die_1.roll()+die_2.roll() for roll_num in range(1000)]
# print(results)

#分析结果
'''
frequences = []


for value in range(2,max_results+1):
    frequence = results.count(value)
    frequences.append(frequence)
'''
max_results = die_1.num_sides + die_2.num_sides
frequences = [results.count(value) for value in range(2,max_results+1)]
#对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D8 dice 1000 times'
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_labels = range(2,max_results+1)
hist.x_title = 'Results'
hist.y_title = 'Frequence of Result'
hist.add('D8+D8', frequences)
hist.render_to_file('2D8_visual.svg')
