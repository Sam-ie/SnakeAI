import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap, BoundaryNorm
import map
from map import Point
import model

# 定义颜色映射
cmap = ListedColormap(['yellow', 'green', 'gray', 'black', 'red'])
bounds = [-3.5, -2.5, -1.5, -0.5, 0.5, 1000.5]
norm = BoundaryNorm(bounds, cmap.N)


# 定义生成器函数
def infinite_frames():
    i = 0

    while True:
        if not snake.move():
            break
        yield i
        i += 1
    yield None  # 这里的 None 或其他值用于通知动画结束


def update(frame):
    if frame is None:  # 检查frame是否为None
        anim.event_source.stop()  # 停止动画
        return [im, score_text]

    # 这里你可以根据需要更新MAP_DATA
    for i in range(len(map.MAP_DATA)):
        for j in range(len(map.MAP_DATA[i])):
            if map.MAP_DATA[i][j] > 0:
                map.MAP_DATA[i][j] -= 1
                if map.MAP_DATA[i][j] == 0:
                    apples.del_and_gen(Point(i, j))

    im.set_data(map.MAP_DATA)  # 更新图像数据

    # 更新分数文本
    score_text.set_text(f"Score: {snake.score}")
    return [im, score_text]


def draw_map():
    global fig, ax, im
    fig, ax = plt.subplots()
    im = ax.imshow(map.MAP_DATA, cmap=cmap, norm=norm)
    ax.axis('off')


if __name__ == '__main__':
    draw_map()
    # 创建一个文本对象来显示分数
    score_text = ax.text(0.5, 0.97, "", transform=ax.transAxes, ha="center")

    apples = model.Apple(map.MAP_DATA, map.num_apples)

    # 使用INITIAL_SNAKE_BODY的第一个元素作为头部，其余作为身体
    head = model.Point(*map.INITIAL_SNAKE_BODY[0])
    body = [model.Point(*pos) for pos in map.INITIAL_SNAKE_BODY[1:]]
    snake = model.Snake(head, body, apples)

    # 创建动画
    anim = FuncAnimation(fig, update, frames=infinite_frames, interval=map.INTERVAL, blit=True)

    plt.show(block=True)
