from time import sleep

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)
        print()

    def strike(self, enemy):
        print(
            '-> УДАР! ' + self.name + ' атакует ' + enemy.name +
            ' с силой ' + str(self.power) + ', используя ' + self.weapon + '\n')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0

        print(enemy.name + ' покачнулся.')
        print('Класс его брони упал до', enemy.armor) 
        print('Уровень здоровья упал до', enemy.health)
        print()
        
print('Средиземье в опасности! На помощь спешит доблестный рыцарь...')
sleep(2)

knight = Hero('Ричард', 50, 25, 20, 'меч')
knight.print_info()

sleep(2)

print('Вдруг из кустов появляется разбойница!')
sleep(2)

rascal = Hero('Хелен', 20, 5, 5, 'лук')
rascal.print_info()

sleep(2)
print('ДА НАЧНЁТСЯ БИТВА!\n')
sleep(2)

knight.strike(rascal)
sleep(2)

knight.strike(rascal)

if rascal.health <= 0:
    print(rascal.name + ' пала в этом нелёгком бою!')

        
