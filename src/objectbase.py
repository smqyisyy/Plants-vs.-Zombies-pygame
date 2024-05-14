# 对象基类，后续的各个角色都基础此类
import image
import time


class ObjectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super().__init__(pathFmt, pathIndex, pos, size, pathIndexCount)
        # 上次替换图片索引的时间
        self.preIndexTime = 0
        # 上次修改位置的时间
        self.prePosTime = 0

    # 利用update方法调用实现图片替换与位置移动
    def update(self):
        self.checkImageIndex()
        self.checkPosition()

    # 实现图片替换帧动画
    def checkImageIndex(self):
        # 防止图片替换过快
        if time.time() - self.preIndexTime <= 0.2:
            return
        self.preIndexTime = time.time()
        # 自驱动替换图片
        idx = self.pathIndex + 1
        idx = idx % self.pathIndexCount
        self.updateIndex(idx)

    # 实现图片自驱动移动
    def checkPosition(self):
        # 防止移动过快
        if time.time() - self.prePosTime <= 0.2:
            return
        self.prePosTime = time.time()
        # 向左移动
        self.doLeft()
