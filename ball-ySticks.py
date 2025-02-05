from matplotlib import pyplot as plt
import math

from numpy import double

plt.gca().set_aspect("equal", adjustable="box")
plt.xlabel("distance (m)")
plt.ylabel("altitude (m)")
plt.grid(True)


class Integrator:
    sum = 0

    def calc(self, x):
        self.sum
        self.sum = self.sum + x

        return self.sum

    def reset(self):
        self.sum = 0


def toComponents(direction, magnitude):
    x_component = magnitude * math.cos(math.radians(direction))
    y_component = magnitude * math.sin(math.radians(direction))

    return x_component, y_component


XDistanceIntegrator = Integrator()
XVeloIntegrator = Integrator()
YDistanceIntegrator = Integrator()
YVeloIntegrator = Integrator()

angle = (double)(input("What is the angle of elevation (in degrees)? "))
magnitude = (double)(input("What is the magnitude? "))

x_component, y_component = toComponents(angle, magnitude)
forceOfGravity = -9.8

xDistance = 0
xVelo0 = x_component
xVelo = x_component
xAccel = 0

yDistance = 0
yVelo0 = y_component
yVelo = y_component
yAccel = forceOfGravity

while yDistance >= 0:
    plt.scatter(xDistance, yDistance, s=10, c="b")
    plt.pause(0.05)

    xDistance = XDistanceIntegrator.calc(xVelo)
    xVelo = XVeloIntegrator.calc(xAccel) + xVelo0

    yDistance = YDistanceIntegrator.calc(yVelo)
    yVelo = YVeloIntegrator.calc(yAccel) + yVelo0

plt.scatter(xDistance, yDistance, s=150, c="r")
plt.show()


# program 2
print("program 2")
i = 0
colors = ["b", "g", "r", "c", "m", "y", "k"]

while i <= 90:
    XDistanceIntegrator.reset()
    XVeloIntegrator.reset()
    YDistanceIntegrator.reset()
    YVeloIntegrator.reset()
    x_component, y_component = toComponents(i, 250)

    xDistance = 0
    xVelo0 = x_component
    xVelo = x_component
    xAccel = 0

    yDistance = 0
    yVelo0 = y_component
    yVelo = y_component
    yAccel = forceOfGravity

    while yDistance >= 0:
        plt.scatter(xDistance, yDistance, s=10, c=colors[(int)(i / 15)])
        plt.pause(0.05)

        xDistance = XDistanceIntegrator.calc(xVelo)
        xVelo = XVeloIntegrator.calc(xAccel) + xVelo0

        yDistance = YDistanceIntegrator.calc(yVelo)
        yVelo = YVeloIntegrator.calc(yAccel) + yVelo0

    plt.scatter(xDistance, yDistance, s=150, c="r")
    i += 15
plt.show()
