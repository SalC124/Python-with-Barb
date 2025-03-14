from matplotlib import pyplot as plt
import math

plt.xlabel("time (seconds)")
plt.ylabel("voltage (blue), current(mA) (red)")


class Integrator:
    sum = 0

    def calc(self, addend):
        self.sum = self.sum + addend
        return self.sum


Integrator1 = Integrator()
R = 10000
C = 470 * 10**-6
V_initial = 5
i = 0
V = 0
Tau = 0
t_constant = 0

for t in range(0, 20):
    i = V / R
    V = 1 / C * Integrator1.calc(-i) + V_initial
    if V <= V_initial * 0.37 and Tau != 1:
        t_constant = t
        Tau += 1
    plt.scatter(t, i * 1000, s=5, c="r")
    plt.scatter(t, V, s=5, c="b")
print("Time constant =", str(t_constant), "s")

# 4.)
print("T = RC\nSo T=(10000)(470E-6)\nT = 4.7s\n")
# 5.)
print("V = V_initial*(e)^(-t/RC)\nV = 5*e^(-t/(10000 * (470E-6)))")
plt.show()
