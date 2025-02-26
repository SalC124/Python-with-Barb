from matplotlib import pyplot as plt
import math

plt.gca().set_aspect("equal", adjustable="box")

# head
for degrees in range(0, 360, 10):
    y = 5 * math.sin(degrees * math.pi / 180)
    x = 5 * math.cos(degrees * math.pi / 180)
    plt.scatter(x, y, s=5, c="r")
    plt.pause(0.01)

# mouth
taperFade = 2
for degrees in range(0 + (10 * taperFade), (180 + 10 - (10 * taperFade)), 10):
    y = 3 * math.sin(degrees * math.pi / 180)
    x = 3 * math.cos(degrees * math.pi / 180)
    plt.scatter(x, -y, s=5, c="r")
    plt.pause(0.01)

# eyes
x_pos = 1.5
y_pos = 1.75

for degrees in range(0, 360, 10):
    y = 1.25 * math.sin(degrees * math.pi / 180)
    x = 0.75 * math.cos(degrees * math.pi / 180)
    plt.scatter(x + x_pos, y + y_pos, s=5, c="r")
    plt.scatter(-(x + x_pos), y + y_pos, s=5, c="r")

    plt.pause(0.01)

# outline
radius = 6
for i in range(-radius, radius + 1, 1):
    y = (radius**2 - i**2) ** 0.5
    plt.scatter(i, y, s=5, c="r")
    plt.scatter(i, -y, s=5, c="r")
    plt.pause(0.01)


plt.show()
