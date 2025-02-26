from math import floor
from matplotlib import pyplot as plt

plt.gca().set_aspect("equal", adjustable="box")


def program1(cycles):
    for i in range(0, (20 * cycles) + 1, 1):
        y = -abs(i - 10 + (floor(i / 20) * -20)) + 10

        print("x", i, "   y", y)

        plt.scatter(i, y, s=5, c="r")
        plt.pause(0.01)
    plt.show()


def program2(cycles):
    for i in range(0, (20 * cycles) + 1, 1):
        y = i % 11

        print("x", i, "   y", y)

        plt.scatter(i, y, s=5, c="r")
        plt.pause(0.01)
    plt.show()


def program4(radius):
    for i in range(-radius, radius + 1, 1):
        y = (radius**2 - i**2) ** 0.5
        print("x", i, "   y", y)

        plt.scatter(i, y, s=5, c="r")
        plt.scatter(i, -y, s=5, c="r")
        plt.pause(0.01)
    plt.show()


# program 1
print("\nprogram 1")
program1(1)

# program 2
print("\nprogram 2")
program2(1)

# program 3
print("\nprogram 3")
program1(3)

# program 4
print("\nprogram 4")
program4(10)
