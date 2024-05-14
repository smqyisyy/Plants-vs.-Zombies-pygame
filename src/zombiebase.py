# 僵尸的基类
import objectbase


class ZombieBase(objectbase.ObjectBase):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super().__init__(pathFmt, pathIndex, pos, size, pathIndexCount)

