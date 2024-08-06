'''
所有可修改的初值
'''
AI_level = 1  # 电脑等级：1-4 (4级没动力实现了，因为DCN模型的实际效果还不如3)
num_apples = 1  # 苹果数量
score_apples = 100  # 苹果分值：1-10000
INTERVAL = 40  # 控制动画帧率

points = [Point(3, 3), Point(7, 5)]  # 障碍点列表
MAP_DATA = generate_map(7 + 2, 7 + 2)  # , points)  # 地图大小

INITIAL_SNAKE_BODY = [[2, 2], [1, 2], [1, 1]]  # 蛇的初始位置
