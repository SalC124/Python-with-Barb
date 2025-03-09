from matplotlib import pyplot as plt

plt.figure(figsize=(10, 5))
plt.axis([0, 10, 0, 20])
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (inches)")
plt.grid(True)

sum = 0
sum2 = 0
sum3 = 0
velocity = 2
acceleration = 2


def theyreInteGrrrreat(x):
    global sum
    sum = sum + x
    return sum


def integrationStation(x):
    global sum2
    sum2 = sum2 + x
    return sum2


def bruh(x):
    global sum3
    sum3 = sum3 + x
    return sum3


print("\nprogram 1")
for t in range(10):
    plt.scatter(t, sum3, s=5, c="b")
    plt.pause(0.25)

    distance = bruh(velocity)

print("\nprogram 2")
for t in range(10):
    plt.scatter(t, sum, s=5, c="r")
    plt.pause(0.25)

    distance = theyreInteGrrrreat(velocity)
    velocity = integrationStation(acceleration)
plt.show()
