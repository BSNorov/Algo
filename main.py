from turtle import Turtle, Screen
from random import randint




class Sprite(Turtle):
    '''Класс для создания движущихся объектов (спрайтов) в игре.
    Наследуется от Turtle.'''
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step  # шаг движения спрайта
        self.points = 0  # очки спрайта


    def move_up(self):
        '''Двигает спрайт вверх.'''
        self.goto(self.xcor(), self.ycor() + self.step)


    def move_down(self):
        '''Двигает спрайт вниз.'''
        self.goto(self.xcor(), self.ycor() - self.step)


    def move_left(self):
        '''Двигает спрайт влево.'''
        self.goto(self.xcor() - self.step, self.ycor())


    def move_right(self):
        '''Двигает спрайт вправо.'''
        self.goto(self.xcor() + self.step, self.ycor())


    def is_collide(self, sprite):
        '''Проверяет столкновение с другим спрайтом.'''
        dist = self.distance(sprite.xcor(), sprite.ycor())
        return dist < 30


    def set_move(self, x_start, y_start, x_end, y_end):
        '''Устанавливает маршрут движения спрайта между двумя точками.'''
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))  # определяем направление движения


    def make_step(self):
        '''Перемещает спрайт на один шаг в заданном направлении.'''
        self.forward(self.step)


        if self.distance(self.x_end, self.y_end) < self.step: # если расстояние до конечной точки меньше шага, меняем направление
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)




# Создание объектов (игрок, враги, цель)
player = Sprite(0, -100, 10, 'circle', 'orange')
enemy1 = Sprite(-200, 0, 15, 'square', 'red')
enemy1.set_move(-200, 0, 200, 0)
enemy2 = Sprite(200, 70, 15, 'square', 'red')
enemy2.set_move(200, 70, -200, 70)
goal = Sprite(0, 120, 20, 'triangle', 'green')


# Очки игрока
total_score = 0


# Настройки экрана
scr = player.getscreen()
scr.listen()


# Управление игроком
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')


# Игровой цикл
while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
   
    if player.is_collide(goal):
        total_score += 1
        player.goto(0, -100)
   
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        player.hideturtle()
        break


# Скрываем все спрайты при достижении цели
if total_score == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
    player.hideturtle()
    goal.hideturtle()
