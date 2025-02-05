from matplotlib import pyplot as plt
import math

plt.figure(figsize=(5, 2.5))

plt.axis([0, 360, -6, 6])

for a in range(0, 360, 10):
    y = 5 * math.sin(a * math.pi / 180)

    print("a", a, "   y", y)

    plt.scatter(a, y, s=5, c="r")
    plt.pause(0.01)
plt.pause(10)
