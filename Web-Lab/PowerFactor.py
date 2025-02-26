from matplotlib import pyplot as plt
import math

loops = 2


def toRad(degNum):
    return degNum * (math.pi / 180)


def toDeg(radNum):
    return radNum * (180 / math.pi)


print("program 1")
amplitude1 = 169.7
for a in range(0, 360 * loops, 10):
    v = amplitude1 * math.sin(a * math.pi / 180)
    plt.scatter(a, v, s=5, c="r")  # plot x,y point with size and color
plt.show()

print("program 2")
amplitude2 = 154.3
for a in range(0, 360 * loops, 10):
    v = amplitude1 * math.sin(a * math.pi / 180)
    plt.scatter(a, v, s=5, c="r")
    i = amplitude2 * math.sin(a * math.pi / 180)
    plt.scatter(a, i, s=5, c="b")
plt.show()

print("program 3")
theta = 45
for a in range(0, 360 * loops, 10):
    v = amplitude1 * math.sin(toRad(a))
    plt.scatter(a, v, s=5, c="r")
    i = amplitude2 * math.sin(toRad(a))
    plt.scatter(a + theta, i, s=5, c="b")
plt.show()

print("program 4")


def powerFactorPlot(powerFactor):
    theta = toDeg(math.acos(powerFactor))
    for a in range(0, 360 * loops, 10):
        v = amplitude1 * math.sin(toRad(a))
        plt.scatter(a, v, s=5, c="r")
        i = amplitude2 * math.sin(toRad(a))
        plt.scatter(a + theta, i, s=5, c="b")
        plt.title(powerFactor)
    plt.show()


powerFactorPlot(1)
powerFactorPlot(0.8)
powerFactorPlot(0.5)
powerFactorPlot(0)
