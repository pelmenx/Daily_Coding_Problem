# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
# Monte Carlo method.
#
# Hint: The basic equation of a circle is x^2 + y^2 = r^2.
#
#
# --------------------------------------------------------------------------------
#
#

# We suppose a circle with radius = 1. It can fit in a square with side length = 2.
# The square corners located in dots [[-1,1],[1,1],[-1,-1],[1,-1]]
import random


def Monte_Carlo_method(number_of_dots, radius):
    count = 0
    for i in range(0, number_of_dots):
        distance = distance_to_point(radius)
        if distance < radius:
            count += 1
    coefficient = count / number_of_dots
    pi = (radius * 2) ** 2 * coefficient
    return(round(pi, 3))


def distance_to_point(radius):
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)
    distance = ((0 - x) ** 2 + (0 - y) ** 2) ** (1 / 2)
    return distance


print(Monte_Carlo_method(100, 1))
print(Monte_Carlo_method(1000, 1))
print(Monte_Carlo_method(10000, 1))
print(Monte_Carlo_method(100000, 1))
