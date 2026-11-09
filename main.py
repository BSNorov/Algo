from turtle import *
from random import randint
from time import sleep

width = 200
height = 250


def start(t, y):
    t.penup()
    t.goto(-1 * width, y)
    t.setheading(0)


def beginstripe(t, x):
    t.speed(25)
    start(t, height)
    t.forward(x)
    t.left(-90)
    t.hideturtle()


def stripe(t, x):
    t.pendown()
    t.forward(2 * height)
    t.penup()
    t.goto(t.xcor() + x, height)


def startrace(t, y):
    start(t, y)
    t.shape('turtle')
    t.showturtle()
    t.speed(5)


def dance(t):
    t.speed(15)
    t.left(randint(0, 90))
    j = 0
    while j < 8:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        i = 1
        while i < 32:
            t.forward(i)
            t.left(i / 2 + 5)
            i += 1
        j += 1
    t.penup()
    t.goto(0, 0)


# Начало основной программы:


# Создаём участников гонки:
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color('red')
t2.color('blue')
t3.color('green')

# рисуем полосы ширины x:
x = 20

beginstripe(t1, 0)
beginstripe(t2, x)
beginstripe(t3, 2 * x)

while t1.xcor() < width and t2.xcor() < width:
    stripe(t1, 3 * x)
    stripe(t2, 3 * x)
    stripe(t3, 3 * x)

# начало гонки
startrace(t1, 20)
startrace(t2, -20)
startrace(t3, -60)

sleep(1)

while t1.xcor() < width and t2.xcor() < width and t3.xcor() < width:
    t1.forward(randint(2, 7))
    t2.forward(randint(2, 7))
    t3.forward(randint(2, 7))
sleep(1)

# подводим итог:
t1.clear()
t2.clear()
t3.clear()

max_x = max(t1.xcor(), t2.xcor(), t3.xcor())

if t1.xcor() == max_x:
    dance(t1)

if t2.xcor() == max_x:
    dance(t2)

if t3.xcor() == max_x:
    dance(t3)
