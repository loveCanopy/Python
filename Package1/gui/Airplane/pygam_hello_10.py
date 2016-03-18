import pygame
import os
from sys import exit 
import random

class Bullet:
    def __init__(self):
        '''初始化子弹坐标并加载子弹图片'''
        self.x = 0
        self.y = -1
        self.image = pygame.image.load(bullet_img).convert_alpha()
        self.active = False

    def move(self):
        '''移动子弹'''
        if self.active:
            self.y -= 3

        if self.y < 0:
            self.active = False

    def restart(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = x - self.image.get_width()/2
        self.y = y - self.image.get_height()/2
        self.active = True

class Enemy:
    def __init__(self):
        self.restart()
        self.image = pygame.image.load(enemy_img).convert_alpha()

    def restart(self):
        self.x = random.randint(50,400)
        self.y = random.randint(-200,-50)
        self.speed = random.random() + 0.1

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()



pygame.init()
bg_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\shoot_background\\background.png'
bg_img2 = 'bg2.jpg'
plane_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\plane.png'
bullet_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\bullet.png'
enemy_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\enemy.png'

screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption('Hello World!')
background = pygame.image.load(bg_img).convert()
plane = pygame.image.load(plane_img).convert_alpha()
bullet = Bullet()
enemy = Enemy()     # 建立敌机

bullets = []
for i in range(5):
    bullets.append(Bullet())

count_b = len(bullets)      # 子弹的总数
index_b = 0         # 即将激活的子弹序号
interval_b = 0      # 发射子弹的间隔

enemies = []
for i in range(5):
    enemies.append(Enemy())

def checkHit(enemy,bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    # 绘画背景
    screen.blit(background,(0, 0))

    # 定位鼠标的x, y坐标
    x, y = pygame.mouse.get_pos()

    # 发射子弹
    interval_b -= 1
    if interval_b < 0:
        bullets[index_b].restart()
        interval_b = 100
        index_b = (index_b + 1) % count_b

    for b in bullets:
        if b.active:
            # 检查子弹命中情况
            for e in enemies:
                checkHit(e, b)
            b.move()
            screen.blit(b.image, (b.x, b.y))




    # 绘画机群
    for e in enemies:
        e.move()
        screen.blit(e.image, (e.x, e.y))

    # 定位并绘画飞机到屏幕上
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    screen.blit(plane, (x, y))
    pygame.display.update()