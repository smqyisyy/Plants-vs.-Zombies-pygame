# 向日葵的类
import objectbase
import sunlight


class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        # 是否已经产生了阳光
        self.hasSunLight = False

    #  召唤阳光
    def preSummon(self):
        self.hasSunLight = True

    @property
    def hasSummon(self):
        return self.hasSunLight

    # 产生阳光
    def doSummon(self):
        if self.hasSummon:
            self.hasSunLight = False
            return sunlight.SunLight(2, (self.pos[0] + 20, self.pos[1] - 10))
