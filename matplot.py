#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:42:07 2021

@author: henryhutchings
"""

import matplotlib.pyplot as plt
import math

# Create x as a list of 300 numbers equally spaced from 0 to 20
numpoints = 300
xmin = 0
xmax = 20
delta_x = (xmax - xmin) / (numpoints - 1)
x = [xmin + i*delta_x for i in range(numpoints)]

# Create y as a list of corresponding y values for y = sin(x)
y = [math.sin(xi) for xi in x]

# Now plot them:
plt.plot(x, y)
plt.show()