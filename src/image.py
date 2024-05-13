# 用于进行图片展示类
import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        # 图片路径格式化字符串
        self.pathFmt = pathFmt
        # 当前图片的下标
        self.pathIndex = pathIndex
        # 所有图片的数量
        self.pathIndexCount = pathIndexCount
        # 图片大小
        self.size = size
        # 图片位置
        self.pos = list(pos)
        self.updateImage()

    # 更新图片的索引,替换图片实现帧动画
    def updateImage(self):
        path = self.pathFmt
        if self.pathIndexCount != 0:
            # 对图片的占位符进行替换
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        # 缩放图片大小到窗口大小
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    # 更新图片size属性
    def updateSize(self, size):
        self.size = size
        self.updateImage()

    # 更新索引
    def updateIndex(self, pathIndex):
        self.pathIndex = pathIndex
        self.updateImage()

    # 获取图片的矩形
    def getRect(self):
        rect = self.image.get_rect()
        rect.x, rect.y = self.pos[0], self.pos[1]
        return rect

    # 图片绘制函数
    def draw(self, ds):
        ds.blit(self.image, self.getRect())

    # 图片平移功能，向左平移
    def doLeft(self):
        self.pos[0] -= 0.3
