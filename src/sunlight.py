# 阳光的类
import objectbase


class SunLight(objectbase.ObjectBase):
    # 自驱动平移
    def checkPosition(self):
        b = super().checkPosition()
        # 如果现在是到了要变的时间，就变
        if b:
            self.pos[1] += 2
        return b
