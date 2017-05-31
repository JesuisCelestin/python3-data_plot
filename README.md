# python3-data_plot
自学 《python编程-从入门到实践 》
## 项目二：数据可视化 15.4 使用 Pygal模拟掷骰子
### step 1 : 命令行 pip install Pygal（前提是已经将python加入到环境path）
### step 2 : 用 die.py 创建 Die 类
这个Die类应该包含骰子的面数，以及一个投掷的方法，这里用randint实现随机的方法roll
### step 3 : 用循环模拟多次投掷
这里可以用 for 循环 也可以用列表解析
### step 4 : 用 hist = pygal.Bar() 画出直方图
