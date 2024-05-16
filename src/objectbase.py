# 对象基类，后续的各个角色都基础此类
import image
import time
import data_object


class ObjectBase(image.Image):
    def __init__(self, id, pos):
        # 数据表中的id
        self.id = id
        # 上次替换图片索引的时间
        self.preIndexTime = 0
        # 上次修改位置的时间
        self.prePosTime = 0
        # 上次召唤时间
        self.preSummonTime = 0
        super().__init__(self.getData()["PATH"], 0, pos, self.getData()["SIZE"], self.getData()["IMAGE_INDEX_MAX"])

    # 通过id拿数据
    def getData(self):
        return data_object.data[self.id]

    # 用于子类实现来设置位置变动的频率避免掉帧
    def getPositionCD(self):
        return self.getData()["POSITION_CD"]

    def getImageIndexCD(self):
        return self.getData()["IMAGE_INDEX_CD"]

    def getSummonCD(self):
        return self.getData()["SUMMON_CD"]

    # 利用update方法调用实现图片替换与位置移动
    def update(self):
        self.checkImageIndex()
        self.checkPosition()
        self.checkSummon()

    # 获取价格
    def getPrice(self):
        return self.getData()["PRICE"]

    # 获取速度
    def getSpeed(self):
        return self.getData()["SPEED"]

    # 判断是否能够被捡起
    def canLoot(self):
        return self.getData()["CAN_LOOT"]

    # 检查是否需要图片替换帧动画
    def checkImageIndex(self):
        # 防止图片替换过快
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            return
        self.preIndexTime = time.time()
        # 自驱动替换图片
        idx = self.pathIndex + 1
        idx = 0 if idx >= self.pathIndexCount else idx
        self.updateIndex(idx)
        return True

    # 检查是否需要图片移动
    def checkPosition(self):
        # 防止移动过快
        if time.time() - self.prePosTime <= self.getPositionCD():
            return
        self.prePosTime = time.time()
        speed = self.getSpeed()
        self.pos = (self.pos[0] + speed[0], self.pos[1] + speed[1])
        return True

    def checkSummon(self):
        # 防止召唤过多
        if time.time() - self.preSummonTime <= self.getSummonCD():
            return
        self.preSummonTime = time.time()
        self.preSummon()

        return True

    # 子类实现召唤自己的召唤物
    def preSummon(self):
        pass
