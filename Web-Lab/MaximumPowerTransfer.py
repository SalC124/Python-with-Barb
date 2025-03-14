from matplotlib import pyplot as plt

plt.figure(figsize=(5, 2.5))  # fix for the bug in repl.it
V_S = 12  # Source Voltage, 12 V
R_S = 4  # Source Resistance, 4 Ohms
maximum = -999
resAtMax = -999
for R_L in range(1, 30):
    i = V_S / (R_S + R_L)
    V_L = i * R_L
    P_L = V_L * i

    if P_L > maximum:
        maximum = P_L
        resAtMax = R_L
    plt.scatter(R_L, i, s=5, c="r")
    # plot current point in red
    plt.scatter(R_L, V_L, s=5, c="g")  # plot voltage point in green
    plt.scatter(R_L, P_L, s=5, c="b")  # plot voltage point in blue
    plt.pause(0.01)  # delay before next point is plotted

plt.show()
print("maximum power load:", maximum)
print("load resistance at max power load:", resAtMax)

# 4) What resistor relationship exists at the maximum power point?
print("source resistance and load resistance are equal (4)")
