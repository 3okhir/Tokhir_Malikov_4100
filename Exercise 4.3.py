# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:31:18 2021

@author: tmali
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

def f(x):
    return x * (x - 1)

def fp(x):
    return 2 * x - 1

def der(f, x, h):
    dv = (f(x + h) - f(x)) / h
    return dv

x = 1
true = fp(x)

hs = [10 ** -(i) for i in range (1, 15, 3)]

derv = [der(f, x, h) for h in hs]

err = [abs(der(f, x, h) - true) for h in hs]

ers = []
for i in err:
    ers.append(i)

plt.plot(np.log(hs), np.log(ers))
plt.xlabel('$\Delta$ h')
plt.ylabel('$\epsilon$, errors')
plt.show()

print("%s seconds" % (time.time() - start_time))

if __name__ == "__main__":


    row = "{0:1.0e} {1:1.18} {2:1.18}"


    for h, dv, err in zip(hs, derv, err):
        print(row.format(h, dv, err))