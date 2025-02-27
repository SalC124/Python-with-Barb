from matplotlib import pyplot as plt

import math

plt.gca().set_aspect("equal", adjustable="box")


def spiralPlot(cycles):
    degree_max = (360 * cycles) + 10
    color1 = "r"
    color2 = "b"
    for degrees in range(0, degree_max, 10):
        if degrees >= degree_max / 2:
            color1 = "b"
            color2 = "r"

        y = degrees * math.sin(degrees * math.pi / 180)
        x = degrees * math.cos(degrees * math.pi / 180)

        print(f"angle = {degrees}\tx = {x}\ty = {y}")
        plt.scatter(x, y, s=5, c=color1)
        plt.scatter(-x, -y, s=5, c=color2)
        # plt.pause(0.01)
    plt.show()


spiralPlot(1)
