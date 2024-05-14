# 射出的子弹类
import objectbase


class PeaBullet(objectbase.ObjectBase):
    def checkPosition(self):
        b = super().checkPosition()
        if b:
            # 右移
            self.doRight()
        return b
