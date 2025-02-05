from matplotlib import pyplot as plt

plt.figure(figsize=(10, 5))
plt.axis([0, 10, 0, 20])
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (inches)")
plt.grid(True)

sum = 0
sum2 = 0
velocity = 0
acceleration = 2


def theyreInteGrrrreat(x):
    global sum
    sum = sum + x
    return sum


def integrationStation(x):
    global sum2
    sum2 = sum2 + x
    return sum2


for t in range(10):
    plt.scatter(t, sum, s=5, c="r")
    plt.pause(0.25)

    distance = theyreInteGrrrreat(velocity)
    velocity = integrationStation(acceleration)
plt.show()
