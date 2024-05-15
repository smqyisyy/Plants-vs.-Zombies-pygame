# 向日葵的类
import objectbase
import sunlight


class SunFlower(objectbase.ObjectBase):
    def __init__(self, id, pos):
        super().__init__(id, pos)
        # 保存自己产生的阳光
        self.sunLights = []

    #  召唤阳光
    def preSummon(self):
        slight = sunlight.SunLight(2, (self.pos[0] + 20, self.pos[1] - 10))
        self.sunLights.append(slight)

    def update(self):
        super().update()
        for sl in self.sunLights:
            sl.update()

    def draw(self,ds):
        super().draw(ds)
        for sl in self.sunLights:
            sl.draw(ds)
