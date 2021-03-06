# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:20:15 2021

@author: tmali
"""

import math
import matplotlib.pyplot as plt

def calculate_y1(w, m, E, h):
    return math.tan(math.sqrt((w * w * m * E) / (2 * h * h)))

def calculate_y2(V, E):
    return math.sqrt((V - E) / E)

def calculate_y3(V, E):
    return -1 / calculate_y2(V, E)

def binarySearch(arr, l, r, x):
    if r >= l:
       mid = l + (r - l) / 2
       if arr[mid] == x:
           return mid
       elif arr[mid] > x:
          return binarySearch(arr, l, mid - 1, x)
       else :
           return binarySearch(arr, mid + 1, r, x) 
    else: 
           return -1

m = 9.1094 / pow(10, 31)
h = 6.62607004 / pow(10, 34)
w = 1.0 / pow(10, 9)
V = 20
E = 1.001
x = []
y1 = []
y2 = []
y3 = []
while (E < 19.999):
   x.append(E)
   y1.append(calculate_y1(w, m, E, h))
   y2.append(calculate_y2(V, E))
   y3.append(calculate_y3(V, E))
   E += 1
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Quantum Theory')
plt.show()
print(x)
print(y1)
print(y2)
print(y3)

    