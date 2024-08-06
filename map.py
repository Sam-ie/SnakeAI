class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def generate_map(h, w, points=None):
    # 如果points没有给出，则使用空列表
    if points is None:
        points = []

    # 创建一个全为-1的边界，并且内部填充为0的二维数组
    map_data = [[-1] * w for _ in range(h)]

    # 填充内部区域为0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            map_data[y][x] = 0

    # 将points中的位置设置为-1
    for point in points:
        if 0 <= point.x < w and 0 <= point.y < h:
            map_data[point.y][point.x] = -1

    return map_data


'''
所有可修改的初值
'''
AI_level = 3  # 电脑等级：1-4
num_apples = 1  # 苹果数量
score_apples = 100  # 苹果分值：1-10000
INTERVAL = 40  # 控制动画帧率

points = [Point(3, 3), Point(7, 5)]  # 障碍点列表
MAP_DATA = generate_map(7 + 2, 7 + 2)  # , points)  # 地图大小

INITIAL_SNAKE_BODY = [[2, 2], [1, 2], [1, 1]]  # 蛇的初始位置

'''
在Python中，当你尝试访问一个二维列表（实际上是列表的列表）中的元素时，
你需要使用两个连续的方括号来指定行和列的索引，而不是用逗号分隔的元组。
'''
MAP_DATA[INITIAL_SNAKE_BODY[0][0]][INITIAL_SNAKE_BODY[0][1]] = -3
for position in INITIAL_SNAKE_BODY[1:]:
    MAP_DATA[position[0]][position[1]] = -2  # 设置初始蛇体位置


def reset_map():
    MAP_DATA = generate_map(7 + 2, 7 + 2)  # , points)  # 地图大小
    MAP_DATA[INITIAL_SNAKE_BODY[0][0]][INITIAL_SNAKE_BODY[0][1]] = -3
    for position in INITIAL_SNAKE_BODY[1:]:
        MAP_DATA[position[0]][position[1]] = -2  # 设置初始蛇体位置
