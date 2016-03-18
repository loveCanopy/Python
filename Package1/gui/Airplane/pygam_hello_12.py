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


class Plane:
    def restart(self):
        self.x = 200
        self.y = 600

    def __init__(self):
        self.restart()
        self.image = pygame.image.load(plane_img).convert_alpha()

    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width() / 2
        y -= self.image.get_height() / 2
        self.x = x 
        self.y = y




pygame.init()
# 图片地址
bg_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\shoot_background\\background.png'
bg_img2 = 'bg2.jpg'
plane_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\plane.png'
bullet_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\bullet.png'
enemy_img = 'E:\\005_python\\sourcecode\\Airplane\\ui\\enemy.png'

# GUI 对象
screen = pygame.display.set_mode((450, 800), 0, 32)
pygame.display.set_caption('一起打飞机')
background = pygame.image.load(bg_img).convert()
plane = pygame.image.load(plane_img).convert_alpha()
font = pygame.font.Font(None, 32)


# 游戏变量
gameover = False
score = 0
bullet = Bullet()
enemy = Enemy()     # 建立敌机
plane = Plane()

bullets = []
for i in range(5):
    bullets.append(Bullet())

count_b = len(bullets)      # 子弹的总数
index_b = 0         # 即将激活的子弹序号
interval_b = 0      # 发射子弹的间隔

enemies = []
for i in range(5):
    enemies.append(Enemy())


# 子弹与敌机 的碰撞检测
def checkHit(enemy, bullet):
    if (bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False

# 我机与敌机 的碰撞检测
def checkCrash(enemy, plane):
    if (plane.x + 0.7 * plane.image.get_width() > enemy.x) and (plane.x + 0.3 * plane.image.get_width() < enemy.x + enemy.image.get_width()) and (plane.y + 0.7 * plane.image.get_height() > enemy.y) and (plane.y + 0.3 * plane.image.get_width() < enemy.y + enemy.image.get_height()):
        return True
    return False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 绘画背景
    screen.blit(background,(0, 0))

    # 检测游戏状态
    if not gameover:

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
                    # 击中敌机，分数加100
                    if checkHit(e, b):
                        score += 100
                b.move()
                screen.blit(b.image, (b.x, b.y))

        # 绘画机群
        for e in enemies:
            e.move()
            screen.blit(e.image, (e.x, e.y))

            if checkCrash(e, plane):
                gameover = True
                
            e.move()
            screen.blit(e.image, (e.x, e.y))

            plane.move()
            screen.blit(plane.image, (plane.x, plane.y))

            # 屏幕左上角显示分数
            text = font.render("Score: %d" % score, 1, (0, 0, 0))
            screen.blit(text, (0, 0))
    else:
        text = font.render("Score: %d" % score, 1, (0, 0, 0))
        screen.blit(text, (190, 400))

    # 游戏结束后，检测鼠标抬起就“重置游戏”
    if gameover and event.type == pygame.MOUSEBUTTONUP:
        plane.restart()
        for e in enemies:
            e.restart()
        for b in bullets:
            b.active = False
        score = 0
        gameover = False
        
    pygame.display.update()