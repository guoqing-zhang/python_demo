# -*- coding: utf-8 -*-
# Created : 2019/12/19 9:21
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn

import turtle

def draw_rectangle(x, y ,width, height):
    """绘制矩形"""
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.endfill()

def draw_star(x, y, radius):
    """绘制五角星"""

    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()

