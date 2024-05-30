# 数据表文件
import os
from math import inf

# 子弹图
pb_path = os.path.abspath("../pic/other/peabullet.png")
# 僵尸图
z_path = os.path.abspath("../pic/zombie/0/%d.png")
# 阳光图
sl_path = os.path.abspath("../pic/other/sunlight/%d.png")
# 向日葵图
sf_path = os.path.abspath("../pic/plant/sunflower/%d.png")
# 豌豆射手图
ps_path = os.path.abspath("../pic/plant/peashooter/%d.png")
data = {
    0: {
        "PATH": pb_path,
        "IMAGE_INDEX_MAX": 0,
        "IMAGE_INDEX_CD": 0,
        "POSITION_CD": 0.008,
        "SIZE": (44, 44),
        "SPEED": (4, 0),
        "SUMMON_CD": inf,
        "CAN_LOOT": False,
        # 价格
        "PRICE": 0,
        # 血量
        "HP": 1,
        # 攻击力
        "ATT": 1
    },
    1: {
        "PATH": z_path,
        # 图片有多少帧
        "IMAGE_INDEX_MAX": 15,
        # 切换图片索引的时间间隔
        "IMAGE_INDEX_CD": 0.2,
        # 位置切换的时间间隔
        "POSITION_CD": 0.2, "SIZE": (100, 128),
        "SPEED": (-2.5, 0),
        # 召唤物的cd
        "SUMMON_CD": inf,
        "CAN_LOOT": False,
        "PRICE": 0,
        # 血量
        "HP": 5,
        # 攻击力
        "ATT": 1
    },
    2: {
        "PATH": sl_path,
        # 图片有多少帧
        "IMAGE_INDEX_MAX": 30,
        # 切换图片索引的时间间隔
        "IMAGE_INDEX_CD": 0.06,
        # 位置切换的时间间隔
        "POSITION_CD": 0.05,
        "SIZE": (80, 80),
        "SPEED": (0, 2),
        # 召唤物的cd
        "SUMMON_CD": inf,
        # 是否可以被捡起
        "CAN_LOOT": True,
        "PRICE": 25,
        "HP": inf,
        "ATT": 0
    },
    3: {
        "PATH": sf_path,
        # 图片有多少帧
        "IMAGE_INDEX_MAX": 19,
        # 切换图片索引的时间间隔
        "IMAGE_INDEX_CD": 0.07,
        # 位置切换的时间间隔
        "POSITION_CD": inf,
        "SIZE": (128, 128),
        "SPEED": (0, 0),
        # 召唤物的cd
        "SUMMON_CD": 8,
        "CAN_LOOT": False,
        "PRICE": 50,
        # 血量
        "HP": 5,
        # 攻击力
        "ATT": 0
    },
    4: {
        "PATH": ps_path,
        # 图片有多少帧
        "IMAGE_INDEX_MAX": 15,
        # 切换图片索引的时间间隔
        "IMAGE_INDEX_CD": 0.15,
        # 位置切换的时间间隔
        "POSITION_CD": inf,
        "SIZE": (128, 128),
        "SPEED": (0, 0),
        # 召唤物的cd
        "SUMMON_CD": 3,
        "CAN_LOOT": False,
        "PRICE": 100,
        # 血量
        "HP": 5,
        # 攻击力
        "ATT": 0
    }
}
