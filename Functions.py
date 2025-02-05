import numpy as np
from matplotlib import pyplot as plt

# grabbed from accuweather for Los Banos on 2025-01-06
temps = [55, 57, 59, 61, 59, 57, 55, 54]

coldTemps = [55, 57, 55, 54]
hotTemps = [59, 61, 59, 57]


# program 1
def avg(listValues):
    total = 0
    for i in range(0, len(listValues)):
        total += listValues[i]
    return total / len(listValues)


print("cold temperatures average:", avg(coldTemps))
print("hot temperatures average:", avg(hotTemps))


# program 2
def min_max(listValues: list, which: str):
    min = 999
    max = -999
    for i in range(0, len(listValues)):
        if listValues[i] < min:
            min = temps[i]
        if listValues[i] > max:
            max = temps[i]
    if which == "min":
        return min
    elif which == "max":
        return max
    else:
        return "learn how to type correctly, you baka"


print(
    "\nCold Temps:\n\tmin:",
    min_max(coldTemps, "min"),
    "\n\tmax:",
    min_max(coldTemps, "max"),
)
print(
    "\nHot Temps:\n\tmin:",
    min_max(hotTemps, "min"),
    "\n\tmax:",
    min_max(hotTemps, "max"),
)


# program 3 and program 4
def getXVals(listValues):
    xVals = [0] * len(listValues)
    for i in range(0, len(listValues) - 1):
        xVals[i] = i
    return xVals


def sigmaPlot(listValues):
    bestFit, y_intercept = np.polyfit(getXVals(listValues), listValues, 1)
    print("best fit slope:", bestFit, "y-intercept:", y_intercept)
    for i in range(0, len(listValues)):
        plt.scatter(i, listValues[i], s=5, c="r")
    bfX = [0, len(listValues) - 1]
    bfY = [y_intercept, (((len(listValues) - 1) * bestFit) + y_intercept)]
    plt.plot(bfX, bfY)
    plt.show()


# program 5
def lineFit(listValues, which):
    n = len(listValues)
    x = getXVals(listValues)
    y = listValues

    sumXY = 0
    sumX = 0
    sumX2 = 0
    sumY = 0
    for i in range(0, n):
        sumX = sumX + x[i]
        sumY = sumY + y[i]
        sumXY = sumXY + x[i] * y[i]
        sumX2 = sumX2 + x[i] * x[i]
        sumXY = sumXY / n
        sumX = sumX / n
        sumY = sumY / n
        sumX2 = sumX2 / n

    # slope
    m = (sumXY - sumX * sumY) / (sumX2 - sumX * sumX)
    # y-intercept
    b = (sumX2 * sumY - sumXY * sumX) / (sumX2 - sumX * sumX)

    if which == "slope":
        return m
    elif which == "y-intercept":
        return b
    else:
        "still cant type, huh"


print("\nmy sigma algorithm:")
print("best fit line slope", lineFit(temps, "slope"))
print("y-intercept", lineFit(temps, "y-intercept"))

# program 4 output
sigmaPlot(temps)
