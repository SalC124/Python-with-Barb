from matplotlib import pyplot as plt
import math

plt.figure(figsize=(5, 2.5))

plt.axis([0, 360, -6, 6])

for x in range(0, 360, 10):
    y = 5 * math.sin(x * math.pi / 180)

    print("x", x, "   y", y)

    plt.scatter(x, y, s=5, c="r")
    plt.pause(0.01)
plt.pause(10)
