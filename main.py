from pygame import *
from random import randint

init()

font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.SysFont('arial', 36)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play(-1)
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_bullet = "bullet.png"
img_hero = "rocket.png"
img_enemy = "ufo.png"

score = 0
goal = 10
lost = 0
max_lost = 3

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.right < win_width:
            self.rect.x += self.speed

        self.rect.clamp_ip(window.get_rect())

    def fire(self):
        bullet = Bullet(
            img_bullet,
            self.rect.centerx - 7,
            self.rect.top,
            15,
            20,
            -15
        )
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global lost

        self.rect.y += self.speed

        if self.rect.top > win_height:
            self.rect.x = randint(0, win_width - self.rect.width)
            self.rect.y = -self.rect.height
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.bottom < 0:
            self.kill()


display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(
    image.load(img_back),
    (win_width, win_height)
)

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()

for i in range(5):
    monster = Enemy(
        img_enemy,
        randint(0, win_width - 80),
        -40,
        80,
        50,
        randint(1, 5)
    )
    monsters.add(monster)

bullets = sprite.Group()

finish = False
run = True

clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE and not finish:
                fire_sound.play()
                ship.fire()

    if not run:
        break

    if not finish:
        window.blit(background, (0, 0))

        ship.update()
        monsters.update()
        bullets.update()

        collides = sprite.groupcollide(monsters, bullets, True, True)

        for c in collides:
            score += 1

            monster = Enemy(
                img_enemy,
                randint(0, win_width - 80),
                -40,
                80,
                50,
                randint(1, 5)
            )
            monsters.add(monster)

        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

        text = font2.render(
            "Счет: " + str(score),
            True,
            (255, 255, 255)
        )
        window.blit(text, (10, 20))

        text_lose = font2.render(
            "Пропущено: " + str(lost),
            True,
            (255, 255, 255)
        )
        window.blit(text_lose, (10, 60))

        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(
                lose,
                lose.get_rect(center=(win_width // 2, win_height // 2))
            )

        elif score >= goal:
            finish = True
            window.blit(
                win,
                win.get_rect(center=(win_width // 2, win_height // 2))
            )

    display.update()
    clock.tick(60)

quit()
