from matplotlib import pyplot as plt

plt.figure(figsize=(10, 5))
plt.axis([-16, 16, 0, 100])
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (inches)")
plt.grid(True)


class Integrator:
    sum = 0

    def calc(self, x):
        self.sum
        self.sum = self.sum + x

        return self.sum


sigmaIntegrator = Integrator()
skibidiIntegrator = Integrator()
Integrator3 = Integrator()
Integrator4 = Integrator()

velocity0 = 0
velocity = 4
acceleration = 2
distance0 = 0
distance = 0

distanceTwo0 = 0
velocityTwo = 100
accelerationTwo = -2

for t in range(20):
    distance = sigmaIntegrator.calc(velocity) + distance0
    velocity = skibidiIntegrator.calc(acceleration) + velocity0

    plt.scatter(t, distance, s=10, c="r")
    plt.scatter(t, velocity, s=10, c="g")

    distanceTwo = Integrator3.calc(velocityTwo) + distanceTwo0
    velocityTwo = Integrator4.calc(accelerationTwo)

    plt.scatter(t, distanceTwo, s=10, c="b")
    plt.scatter(-t, distanceTwo, s=10, c="b")

    plt.pause(0.25)
plt.show()
