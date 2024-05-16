import sys
import pygame
from const import *
import zombiebase
import peabullet
import game

# pygame实例化
pygame.init()
# 创建一个1280x600的窗口
DS = pygame.display.set_mode(GAME_SIZE)
game = game.Game(ds=DS)
# 加载僵尸图片
zom = zombiebase.ZombieBase(1, (1080, 200))
# 加载子弹图片
pb = peabullet.PeaBullet(0, (0, 200))

while True:
    # 操作系统接收pygame中的一些事件
    for event in pygame.event.get():
        # 如果用户点击关闭按钮就退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 接收鼠标事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.mouseClickHandler(event.button)
    # 游戏窗口变为全白
    DS.fill((255, 255, 255))
    game.draw()
    game.update()
    # 重新渲染
    pygame.display.update()
