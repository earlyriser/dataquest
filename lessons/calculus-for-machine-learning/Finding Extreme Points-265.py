## 3. Differentiation ##

import matplotlib.pyplot as plt
import numpy as np

x = numpy.linspace(-5,6,110)
y = -(2*x) + 3

plt.plot(x,y)

## 6. Power Rule ##

derivative_one = "5x^4"
derivative_two = "9x^8"
slope_one = 80
slope_two = 0

x1= 2
x2= 0
slope_one = 5*(x1**4)
slope_two = 9*(x2**8)

## 7. Linearity Of Differentiation ##

derivative_3 = "5x^4 -1"
derivative_4 = "3x^2 - 2x"

x3= 1
x4= 2
slope_three = (5*(x3**4)) - 1
slope_four = (3*(x4**2)) - (2*x4)

## 8. Practicing Finding Extreme Values ##

derivative = "3x^2 - 2x"
critical_points = [0, 2/3]
rel_min = [2/3]
rel_max = [0]