# 游戏主逻辑
import pygame

import image

from const import *
import sunflower


class Game:
    def __init__(self, ds):
        self.ds = ds
        # 背景图
        self.back = image.Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
        # 所有的植物
        self.plants = []
        # 召唤物
        self.summons = []
        # 二维数组表示网格中是否有植物
        self.hasPlant = []
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    def draw(self):
        self.back.draw(self.ds)
        for pl in self.plants:
            pl.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)

    def update(self):
        self.back.update(self.ds)
        for pl in self.plants:
            pl.update()
            if pl.hasSummon:
                summon = pl.doSummon()
                self.summons.append(summon)
        for summon in self.summons:
            summon.update()

    # 添加向日葵的方法，x,y代表是哪个格子而不是坐标
    def addSunFlower(self, x, y):
        # 已经有植物了
        if self.hasPlant[x][y]:
            return
        self.hasPlant[x][y] = 1
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflower.SunFlower(3, pos)
        self.plants.append(sf)

    # 根据鼠标位置获取所选中的网格索引
    def getIndexByPos(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    def checkLoot(self, mousePos):
        pass

    def checkAddPlant(self, mousePos, objId):
        x, y = self.getIndexByPos(mousePos)
        # 只能加在绿色网格中
        if x >= GRID_COUNT[0] or x < 0 or y > GRID_COUNT[1] or y < 0:
            return
        if objId == SUNFlOWER_ID:
            self.addSunFlower(x, y)

    # 处理鼠标事件
    def mouseClickHandler(self, btn):
        # 获取鼠标位置
        mousePos = pygame.mouse.get_pos()
        # btn=1为左键按下
        if btn == 1:
            # 是否可以捡阳光
            self.checkLoot(mousePos)
            # 是否要添加植物
            self.checkAddPlant(mousePos, SUNFlOWER_ID)
