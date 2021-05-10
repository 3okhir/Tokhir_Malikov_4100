# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:22:27 2021

@author: tmali
"""

import numpy as np 
import matplotlib.pyplot as plt 
from numpy.random import random

'''
This program approximates the solution using importance sampling with a weight of
w(x) = 1/sqrt(x)
and the transformation of the probability distribution:
P(x) = 1/2*np.sqrt(x) which integrates to sqrt(x) = z
The inverse of the equation is z**2 and generates random values of x. 
The integral is the general weighted average <g>_w, the sum of lambda x divided by 2*N 
using the monte carlo method. 
'''
g = lambda x: 1/(1+ np.e**x)

N = 10000000

# N number of points between 0 and 1
z = np.random.random(N)

# the inverse of sqrt(x)= z is z**2 = x
x = z**2

plt.title(r'$\mathrm{Probability\ Density\ Plot:}\ x = z^2 $')
plt.xlabel('bounds: [0,1]')
plt.ylabel('Probability')
plt.hist(x)
plt.show()

# general weighted average <g>_w 
integral = np.sum(g(x))/N*2

print('Approximation of ', integral)