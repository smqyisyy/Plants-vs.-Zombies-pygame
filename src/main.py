import sys
import pygame
import image
from const import *
import objectbase

# pygame实例化
pygame.init()
# 创建一个1280x600的窗口
DS = pygame.display.set_mode(GAME_SIZE)

# pygame加载背景图片
img = image.Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
# 加载僵尸图片
zom = objectbase.ObjectBase("../pic/zombie/0/%d.png", 0, (1200, 200), (100, 128), 15)
while True:
    # 操作系统接收pygame中的一些事件
    for event in pygame.event.get():
        # 如果用户点击关闭按钮就退出
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 游戏窗口变为全白
    DS.fill((255, 255, 255))
    # 显示背景图片到屏幕
    img.draw(DS)
    # 僵尸自己动
    zom.update()
    zom.draw(DS)
    # 重新渲染
    pygame.display.update()
