# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:34:56 2021

@author: tmali
"""

import numpy as np
import matplotlib.pyplot as plt

th = np.linspace(0, 10*np.pi, 2000)
r1 = th **2
x1 = r1 * np.cos(th)
y1 = r1 * np.sin(th)

plt.plot(x1, y1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

theta_pol = np.linspace(0, 10*np.pi, 2000)
r1 = theta_pol ** 2

x1 = r1 * np.cos(theta_pol)
y1 = r1 * np.sin(theta_pol)

plt.plot(x1,y1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


theta_fey = np.linspace(0, 24 * np.pi, 2000)
r2 = np.exp(np.cos(theta_fey)) - 2 * np.cos(4 * theta_fey) + np.sin(theta_fey / 12) ** 5
x2 = r2 * np.cos(theta_fey)
y2 = r2 * np.sin(theta_fey)

plt.plot(x2,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()