from matplotlib import pyplot as plt

temps = [ 41, 39, 35, 36, 34, 32, 33, 26, 34, 36 ]
numTemps = len(temps)

# program 1
print("\nprogram 1")
tempsTotal = 0
for i in range (0, numTemps):
    tempsTotal += temps[i]
tempAvg = tempsTotal / numTemps
print(tempAvg)

# program 3 and 4
print("\nprograms 3 and 4")
min = 999
max = -999
for i in range (0, numTemps):
    if (temps[i] < min):
        min = temps[i]
    if (temps[i] > max):
        max = temps[i]
mean = (min + max) / 2
print("min: ", min)
print("max: ", max)
print("mean: ", mean)

# program 2/5
print("\nprogram 2/5")
for i in range (0, numTemps):
    if (temps[i] >= mean):
        color = 'r'
    else:
        color = 'b'
    plt.scatter(i, temps[i], s=5, c=color)
plt.show()
print("done.")
