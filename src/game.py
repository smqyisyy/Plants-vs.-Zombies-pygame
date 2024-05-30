# 游戏主逻辑
import random
import time

import pygame

import image

from const import *
import sunflower
import data_object
import peashooter
import zombiebase


class Game:
    def __init__(self, ds):
        self.ds = ds
        # 背景图
        self.back = image.Image(PATH_BACK, 0, (0, 0), GAME_SIZE, 0)
        # 所有的植物
        self.plants = []
        # 僵尸列表
        self.zombies = []
        # 召唤物
        self.summons = []
        # 二维数组表示网格中是否有植物
        self.hasPlant = []
        # 上次产生僵尸的时间
        self.zombieGenerateTime = 0
        # 初始金币
        self.gold = 100
        # 文字字体
        self.goldFont = pygame.font.Font(None, 60)
        # 击败僵尸数
        self.zombie = 0
        # 文字字体
        self.zombieFont = pygame.font.Font(None, 60)
        for i in range(GRID_SIZE[0]):
            col = []
            for j in range(GRID_SIZE[1]):
                col.append(0)
            self.hasPlant.append(col)

    # 渲染字体
    def renderFont(self):
        # 调用pygame中文字的渲染方法，参数antialias为抗锯齿
        textImg = self.goldFont.render("Gold:" + str(self.gold), True, (0, 0, 0))
        # 渲染位置在左上坐标13,23
        self.ds.blit(textImg, (13, 23))
        # 渲染一个白色位置稍作偏移实现阴影效果
        textImg = self.goldFont.render("Gold:" + str(self.gold), True, (255, 255, 255))
        self.ds.blit(textImg, (10, 20))
        textImg = self.zombieFont.render("Score:" + str(self.zombie), True, (0, 0, 0))
        # 渲染位置在左上坐标13,23
        self.ds.blit(textImg, (13, 83))
        # 渲染一个白色位置稍作偏移实现阴影效果
        textImg = self.zombieFont.render("Score:" + str(self.zombie), True, (255, 255, 255))
        self.ds.blit(textImg, (10, 80))

    def draw(self):
        self.back.draw(self.ds)
        for pl in self.plants:
            pl.draw(self.ds)
        for summon in self.summons:
            summon.draw(self.ds)
        for zombie in self.zombies:
            zombie.draw(self.ds)
        self.renderFont()

    def update(self):
        self.back.update(self.ds)
        for pl in self.plants:
            pl.update()
            if pl.hasSummon:
                summon = pl.doSummon()
                self.summons.append(summon)
        for summon in self.summons:
            summon.update()
        for zombie in self.zombies:
            zombie.update()
        #  产生僵尸的时间到了就产生
        if time.time() - self.zombieGenerateTime > ZOMBIE_BORN_CD:
            self.zombieGenerateTime = time.time()
            self.addZombie(ZOMBIE_BORN_X, random.randint(0, GRID_COUNT[1] - 1))
        # 检查是否有僵尸死亡,将对应列表中的数据移除
        self.checkSummonVSZombie()
        # 检查是否有植物死亡，将对应植物列表中的数据移除
        self.checkZombieVsPlant()
        # 如果召唤物超出屏幕应该从内存中销毁
        for summon in self.summons:
            if summon.getRect().x > GAME_SIZE[0] or summon.getRect().y > GAME_SIZE[1]:
                self.summons.remove(summon)
                # break是因为防止remove元素后，后面元素会前移进而导致出现错误
                break

    # 子弹碰撞到僵尸的逻辑
    def checkSummonVSZombie(self):
        for summon in self.summons:
            for zombie in self.zombies:
                # 如果召唤物和僵尸发生碰撞进行攻击逻辑
                if summon.isCollide(zombie):
                    self.fight(summon, zombie)
                    if zombie.hp <= 0:
                        self.zombies.remove(zombie)
                        # 击败僵尸计分
                        self.zombie += 1
                    if summon.hp <= 0:
                        self.summons.remove(summon)
                    return

    # 僵尸吃植物
    def checkZombieVsPlant(self):
        for zombie in self.zombies:
            for plant in self.plants:
                if zombie.isCollide(plant):
                    self.fight(zombie, plant)
                    if plant.hp <= 0:
                        self.plants.remove(plant)
                        return

    # 添加僵尸的方法
    def addZombie(self, x, y):
        # 生成一个僵尸
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        zombie = zombiebase.ZombieBase(1, pos)
        self.zombies.append(zombie)

    # 添加向日葵的方法，x,y代表是哪个格子而不是坐标
    def addSunFlower(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        sf = sunflower.SunFlower(3, pos)
        self.plants.append(sf)

    # 添加豌豆射手方法，x,y代表是哪个格子而不是坐标
    def addPeaShooter(self, x, y):
        pos = LEFT_TOP[0] + x * GRID_SIZE[0], LEFT_TOP[1] + y * GRID_SIZE[1]
        ps = peashooter.PeaShooter(4, pos)
        self.plants.append(ps)

    # 根据鼠标位置获取所选中的网格索引
    def getIndexByPos(self, pos):
        x = (pos[0] - LEFT_TOP[0]) // GRID_SIZE[0]
        y = (pos[1] - LEFT_TOP[1]) // GRID_SIZE[1]
        return x, y

    # 攻击
    def fight(self, a, b):
        while True:
            a.hp -= b.attack
            b.hp -= a.attack
            if b.hp <= 0:
                return True
            if a.hp <= 0:
                return False
        return False

    # 检查能不能捡起来
    def checkLoot(self, mousePos):
        for summon in self.summons:
            # 如果不能捡起
            if not summon.canLoot():
                continue
            # 获取对象矩形
            rect = summon.getRect()
            # 如果点击位置在矩形内,捡起来
            if rect.collidepoint(mousePos):
                self.summons.remove(summon)
                self.gold += summon.getPrice()
                return True
        return False

    def checkAddPlant(self, mousePos, objId):
        x, y = self.getIndexByPos(mousePos)
        # 只能加在绿色网格中
        if x >= GRID_COUNT[0] or x < 0 or y > GRID_COUNT[1] or y < 0:
            return False
        # 如果钱不够也不能加
        if self.gold < data_object.data[objId]["PRICE"]:
            return False
            # 已经有植物了
        if self.hasPlant[x][y]:
            return False
        self.gold -= data_object.data[objId]["PRICE"]
        self.hasPlant[x][y] = 1
        if objId == SUNFlOWER_ID:
            self.addSunFlower(x, y)
        elif objId == PEASHOOTER_ID:
            self.addPeaShooter(x, y)

    # 处理鼠标事件
    def mouseClickHandler(self, btn):
        # 获取鼠标位置
        mousePos = pygame.mouse.get_pos()
        # 捡了那就不能再种植了
        if self.checkLoot(mousePos):
            return True
        # btn=1为左键按下
        if btn == 1:
            # 是否可以捡阳光
            self.checkLoot(mousePos)
            # 是否要添加植物
            self.checkAddPlant(mousePos, SUNFlOWER_ID)
        # btn=3为右键,2是滚轮
        elif btn == 3:
            # 是否要添加植物
            self.checkAddPlant(mousePos, PEASHOOTER_ID)
