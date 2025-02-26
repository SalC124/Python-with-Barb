import numpy as np
import matplotlib.pyplot as plt

# Temperature data
highTemperatures = [63, 66, 64, 61, 62, 57, 59]
lowTemperatures = [35, 41, 33, 29, 31, 32, 35]

# X values (days)
x_values = np.array([0, 1, 2, 3, 4, 5, 6])

# Compute linear regression (best fit line)
m, b = np.polyfit(x_values, highTemperatures, 1)
print(f"y = {m:.4f}x + {b:.4f}")


# Function to compute min and max values
def maxMin(listValues):
    maximum = listValues[0]
    minimum = listValues[0]

    for value in listValues[1:]:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value

    return minimum, maximum


# Compute min and max values for both lists
minHigh, maxHigh = maxMin(highTemperatures)
minLow, maxLow = maxMin(lowTemperatures)

print("MinHigh = %5.1f" % minHigh, "MaxHigh = %5.1f" % maxHigh)
print("MinLow = %5.1f" % minLow, "MaxLow = %5.1f" % maxLow)

# Plot the scatter plot of high temperatures
plt.scatter(x_values, highTemperatures, color="blue", label="High Temperatures")

# Plot the best-fit line
plt.plot(x_values, m * x_values + b, color="red", label="Best Fit Line")

# Labels and title
plt.xlabel("Days")
plt.ylabel("Temperature (°F)")
plt.title("High Temperatures and Best Fit Line")
plt.legend()

# Show the plot
plt.show()
