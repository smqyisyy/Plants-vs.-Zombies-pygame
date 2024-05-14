# 数据表文件
import os

# 子弹图
p_path = os.path.abspath("../pic/other/peabullet.png")
# 僵尸图
z_path = os.path.abspath("../pic/zombie/0/%d.png")

data = {
    0: {
        "PATH": p_path,
        "IMAGE_INDEX_MAX": 0,
        "IMAGE_INDEX_CD": 0,
        "POSITION_CD": 0.008,
        "SIZE": (44, 44)
    },
    1: {
        "PATH": z_path,
        # 图片有多少帧
        "IMAGE_INDEX_MAX": 15,
        # 切换图片索引的时间间隔
        "IMAGE_INDEX_CD": 0.2,
        # 位置切换的时间间隔
        "POSITION_CD": 0.2, "SIZE": (100, 128)
    }
}
