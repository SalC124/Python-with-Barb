import numpy as np
import matplotlib.pyplot as plt

# Data points
yValues = [101, 99, 94, 90, 89, 83, 81]
xValues = [0, 1, 2, 3, 4, 5, 6]


# Function to calculate the best-fit line (Linear Regression)
def LineFit(xValues, yValues):
    sumY = 0
    sumX = 0
    sumX2 = 0
    sumXY = 0

    n = len(yValues)

    for i in range(n):
        sumX += xValues[i]
        sumY += yValues[i]
        sumXY += xValues[i] * yValues[i]
        sumX2 += xValues[i] * xValues[i]

    # Compute means
    sumXY /= n
    sumX /= n
    sumY /= n
    sumX2 /= n

    # Compute slope (m) and y-intercept (b)
    m = (sumXY - sumX * sumY) / (sumX2 - sumX * sumX)
    b = (sumX2 * sumY - sumX * sumXY) / (sumX2 - sumX * sumX)

    return m, b


# Get slope and intercept
m, b = LineFit(xValues, yValues)

# Print results
print("Slope: %2.2f" % m, "Y-Intercept: %2.2f" % b)

# Plot scatter points
plt.scatter(xValues, yValues, color="blue", label="Data Points")

# Plot best-fit line
best_fit_y = [m * x + b for x in xValues]  # Calculate y-values for the line
plt.plot(xValues, best_fit_y, color="red", label="Best Fit Line")

# Labels and title
plt.xlabel("X Values (Days)")
plt.ylabel("Y Values (Temperature, etc.)")
plt.title("Scatter Plot with Best Fit Line")
plt.legend()

# Show the plot
plt.show()
