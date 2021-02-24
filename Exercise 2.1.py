# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:09:55 2021

@author: tmali
"""

import math
import sys

h = float(input("Enter the height: "))

t = math.sqrt(2*h/9.8)

t = float("{0:.3f}".format(t))

print("Time taken is: ",t)