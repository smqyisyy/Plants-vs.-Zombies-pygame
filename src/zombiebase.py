# 僵尸的基类
import objectbase


class ZombieBase(objectbase.ObjectBase):
    # 自驱动平移
    def checkPosition(self):
        b = super().checkPosition()
        # 如果现在是到了要变的时间，就变
        if b:
            self.doLeft()
        return b
