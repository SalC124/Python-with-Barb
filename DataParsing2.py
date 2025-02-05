import numpy as np
from matplotlib import pyplot as plt

lavender = "#b4befe"
pink = "#f5c2e7"

# "SalCali" in decimal form
asciiName = "83,97,108,67,97,108,105"


# program 1
print("\nprogram 1\n")


def stringToIntArray(listValues):
    snippet = ""
    valueList = []
    for i in range(0, len(listValues)):
        if listValues[i] == ",":
            valueList.append(int(snippet))
            snippet = ""
        else:
            snippet += listValues[i]
    return valueList


print(stringToIntArray(asciiName))


# program 2 & 3
print("\nprogram 2 & 3\n")


def plotName(listValues):
    length = len(listValues)

    xVals = [0] * length
    for i in range(0, length - 1):
        xVals[i] = i

    for i in range(0, length):
        plt.scatter(i, listValues[i], c=lavender)

    bestFit, y_intercept = np.polyfit(xVals, listValues, 1)
    bfX = [0, length - 1]
    bfY = [y_intercept, ((length - 1) * bestFit) + y_intercept]
    plt.plot(bfX, bfY, c=pink)
    plt.show()


plotName(stringToIntArray(asciiName))
