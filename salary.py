import matplotlib.pyplot as plt
import numpy as np

data = {
    1.2: 39344,
    1.4: 46206,
    1.6: 37732,
    2.1: 43526,
    2.3: 39892,
    3: 56643,
    3.1: 60151,
    3.3: 54446,
    3.8: 57190,
    4: 63219,
    4.1: 55795,
    4.2: 57082,
    4.66: 1112,
    5: 67939,
    5.2: 66030,
    5.4: 83089,
    6: 81364,
    6.1: 93941,
    6.9: 91739,
    7.2: 98274,
    8: 101303,
    8.3: 113813,
    8.8: 109432,
    9.1: 105583,
    9.6: 116970,
    9.7: 112636,
    10.4: 122392,
    10.6: 121873
}

x_values = list(data.keys())
y_values = list(data.values())

coefficients = np.polyfit(x_values, y_values, 1)
slope = coefficients[0]
intercept = coefficients[1]
line_of_best_fit = [slope * x + intercept for x in x_values]


plt.scatter(x_values, y_values, color='skyblue', label='Salary')


plt.plot(x_values, line_of_best_fit, color='red', linestyle='--')


plt.xlabel("Job Experience")
plt.ylabel("Salary")
plt.title("Linear Regression of Salary")

plt.show()
