from turtle import *

def rect(w, h):
    for i in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)

def sun():
    speed(10)
    color('gold')
    pensize(2)
    penup()
    goto(130, 190)
    pendown()
    begin_fill()
    for i in range(18):
        forward(90)
        left(100)
    end_fill()
    goto(146, 206)
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(55)
        left(100)
    end_fill()


def background():
    speed(10)
    penup()
    goto(-400, 0)
    pendown()
    begin_fill()
    color('skyblue')
    goto(400, 0)
    goto(400, 400)
    goto(-400, 400)
    goto(-400, 0)
    end_fill()

    penup()
    goto(-400, 0)
    pendown()
    color('olivedrab')
    begin_fill()
    goto(400, 0)
    goto(400, -300)
    goto(-400, -300)
    goto(-400, 0)
    end_fill()

    penup()
    goto(-400, -70)
    pendown()
    color('yellowgreen')
    begin_fill()
    goto(400, -70)
    goto(400, -300)
    goto(-400, -300)
    goto(-400, -70)
    pendown()
    end_fill()

    penup()
    goto(-400, -150)
    pendown()
    color('greenyellow')
    begin_fill()
    goto(400, -150)
    goto(400, -300)
    goto(-400, -300)
    goto(-400, -150)
    pendown()
    end_fill()


def building1():
    pensize(4)
    color('darkorchid')
    speed(10)

    begin_fill()
    rect(168, 264)
    end_fill()

    color('darkviolet')
    begin_fill()
    rect(70, 264)
    end_fill()

    left(90)
    forward(96)

    color('rebeccapurple')
    right(180)
    forward(96)
    left(90)
    forward(168)
    left(90)
    forward(96)
    left(90)
    for i in range(4):
        forward(168)
        right(90)

    penup()
    left(90)
    forward(24)
    right(90)
    forward(24)
    pendown()
    window2()

    penup()
    right(90)
    forward(96)
    left(90)
    pendown()
    window1()

    penup()
    forward(72)
    pendown()
    window1()

    penup()
    right(90)
    for i in range(2):
        forward(72)
        right(90)
    right(90)
    pendown()
    window2()


def building2():
    pensize(2)
    color('rebeccapurple')
    speed(10)

    begin_fill()
    rect(150, 250)
    end_fill()

    forward(25)
    left(90)
    forward(25)

    color('lightsteelblue')
    begin_fill()
    rect(85, 100)
    end_fill()

    penup()
    forward(115)
    pendown()

    begin_fill()
    rect(85, 100)
    end_fill()


def window1():
    pensize(4)

    color('skyblue')
    begin_fill()
    rect(48, 48)
    end_fill()

    color('powderblue')
    begin_fill()
    rect(24, 24)
    end_fill()

    color('cadetblue')
    rect(48, 48)


def window2():
    pensize(4)

    color('skyblue')
    begin_fill()
    rect(120, 48)
    end_fill()

    color('powderblue')
    begin_fill()
    rect(80, 24)
    end_fill()

    color('cadetblue')
    rect(120, 48)


def shop():
    pensize(4)
    color('chocolate', 'darkorange')
    speed(10)

    begin_fill()
    rect(200, 115)
    forward(18)
    end_fill()

    color('chocolate', 'orange')
    begin_fill()
    rect(108, 92)
    end_fill()

    forward(24)
    color('grey', 'lightgray')
    begin_fill()
    rect(60, 75)
    end_fill()

    forward(30)
    left(90)
    forward(75)

    penup()
    forward(42)
    left(90)
    pendown()
    color('brown', 'indianred')
    begin_fill()
    forward(79)
    right(135)
    forward(54)
    right(45)
    forward(137)
    right(45)
    forward(53)
    right(135)
    forward(136)
    end_fill()

    penup()
    right(180)
    forward(71)
    right(90)
    forward(17)
    left(90)
    forward(50)
    right(90)
    pendown()
    color('skyblue')
    begin_fill()
    rect(91, 50)
    end_fill()

    color('powderblue')
    begin_fill()
    rect(55, 25)
    end_fill()

    color('cadetblue')
    rect(91, 50)
