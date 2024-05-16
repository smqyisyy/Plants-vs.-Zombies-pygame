# 豌豆射手的类
import time

import objectbase
import peabullet


class PeaShooter(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        # 是否已经产生了子弹
        self.hasBullet = False
        # 是否可以射击(有没有到喷出的那个图)
        self.hasShoot = False

    #  召唤子弹
    def preSummon(self):
        self.hasShoot = True
        self.pathIndex = 0

    @property
    def hasSummon(self):
        return self.hasBullet

    # 产生子弹
    def doSummon(self):
        if self.hasSummon:
            self.hasBullet = False
            return peabullet.PeaBullet(0, (self.pos[0] + self.size[0] - 10, self.pos[1] + 30))

    # 检查是否需要图片替换帧动画
    def checkImageIndex(self):
        # 防止图片替换过快
        if time.time() - self.preIndexTime <= self.getImageIndexCD():
            return
        self.preIndexTime = time.time()
        # 自驱动替换图片
        idx = self.pathIndex + 1
        if idx == 8 and self.hasShoot:
            self.hasBullet = True
        # 没到要发射的时机,从9号图片开始放
        if idx >= self.pathIndexCount:
            idx = 9
        self.updateIndex(idx)
        return True
