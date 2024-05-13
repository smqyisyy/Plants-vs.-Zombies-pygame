import sys

import pygame

# pygame实例化
pygame.init()
# 创建一个1280x600的窗口
size = (1280, 600)
DS = pygame.display.set_mode(size)
import image

# pygame加载背景图片
img = image.Image("../pic/other/back.png", 0, (0, 0), size, 0)
# 加载僵尸图片
img1 = image.Image("../pic/zombie/0/%d.png", 0, (1280, 200), (100, 128), 15)
# image = pygame.image.load("../pic/other/back.png")
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
    # 僵尸左移
    img1.doLeft()
    # 僵尸图片替换
    img1.updateIndex((img1.pathIndex + 1) % 15)
    img1.draw(DS)
    # DS.blit(image, image.get_rect())
    # 重新渲染
    pygame.display.update()
