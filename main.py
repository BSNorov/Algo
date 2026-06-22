from turtle import *
from random import randint
from time import sleep

w = 200
h = 200
margin = 30

t1 = Turtle()
t1.shape('turtle')
t1.color('red')
t1.speed(15)
t1.points = 0
t1.penup()

t2 = Turtle()
t2.shape('turtle')
t2.color('blue')
t2.speed(10)
t2.points = 0
t2.penup()


def rand_move(t):
    x = randint(-w + margin, w -margin)
    y = randint(-h + margin, h - margin)
    t.goto(x, y)

def catch1(x, y):
    t1.points += 1
    t1.write('A!', font=("Arial", 14, 'normal'))
    print('Очки красной черепашки:', t1.points)

    if t1.points >= 3:
        t1.hideturtle()
        t1.goto(0, 20)
        t1.write('WOW!', align='center', font=("Arial", 14, 'bold'))

def catch2(x, y):
    t2.points += 1
    t2.write('A!', font=("Arial", 14, 'normal'))
    print('Очки синей черепашки:', t2.points)

    if t2.points >= 3:
        t2.hideturtle()
        t2.goto(0, -20)
        t2.write('WOW!',  align='center', font=("Arial", 14, 'bold'))

t1.onclick(catch1)
t2.onclick(catch2)

while t1.points < 3 or t2.points < 3:
    if t1.points < 3:
        rand_move(t1)
    
    if t2.points < 3:
        rand_move(t2)

    sleep(1)

print("Игра окончена!")    
exitonclick()
