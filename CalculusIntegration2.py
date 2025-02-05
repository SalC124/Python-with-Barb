from matplotlib import pyplot as plt

plt.figure(figsize=(10, 5))
plt.axis([0, 10, 0, 100])
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (inches)")
plt.grid(True)


class Integrator:
    sum = 0

    def calc(self, x):
        self.sum
        self.sum = self.sum + x

        return self.sum


Integrator1 = Integrator()
Integrator2 = Integrator()
Integrator3 = Integrator()
Integrator4 = Integrator()

velocity0 = 0
velocity = 4
acceleration = 2
distance0 = 0
distance = 0

velocityTwo0 = 4
velocityTwo = 2
accelerationTwo = -2
distanceTwo0 = 16
distanceTwo = 0

for t in range(20):
    distance = Integrator1.calc(velocity) + distance0
    velocity = Integrator2.calc(acceleration) + velocity0

    plt.scatter(t, distance, s=10, c="r")

    distanceTwo = Integrator3.calc(velocityTwo) + distanceTwo0
    velocityTwo = Integrator4.calc(accelerationTwo) + velocityTwo0

    plt.scatter(t, distanceTwo, s=10, c="b")

    plt.pause(0.25)
plt.show()
