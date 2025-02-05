from matplotlib import pyplot as plt
import math

plt.figure(figsize=(0, 60))

plt.axis([0, 360, -6, 6])

for x in range(0, 11, 1):
    y = x

    print("x", x, "   y", y)

    plt.scatter(x, y, s=5, c="r")
    plt.pause(0.01)
plt.pause(10)
