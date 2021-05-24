# -*- coding: utf-8 -*-
"""
Created on Mon May 24 18:14:40 2021

@author: tmali
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as am
from scipy.linalg import solve_banded

N = 1000        
L = 1.0e-8      
x0 = L/2.0      
sigma = 1.0e-10 
k = 5.0e10      
M = 9.109e-31   
a = L/N          
hbar = 6.62e-34 
h = 1e-19       
tf = 4.0e-16    


V = np.zeros(N+1, complex)
x = np.linspace(0, L, N+1)
psi0 = np.zeros(N+1, complex)
psi0[0:N+1] = np.exp(-(x[0:N+1] - x0)**2/(2*sigma*sigma)) * np.exp(k*x[0:N+1]*1j)


a1 = complex(1, h*hbar/(2*M*a*a))
a2 = complex(0, -h*hbar/(4*M*a*a))
b1 = complex(1, -h*hbar/(2*M*a*a))
b2 = complex(0, h*hbar/(4*M*a*a))


A = np.zeros([3, N+1], complex)
A[0,:] = a2
A[1,:] = a1
A[2,:] = a2


def waves(_V, _psi0):
    V[1:N] = b1*_psi0[1:N] + b2*(_psi0[2:N+1] + _psi0[0:N-1])
    psi = solve_banded((1,1),A, V)
    return V, psi
    

real_parts = []
t = 0
while t < tf:
    V, psi = waves(V, psi)
    real_part = psi.real
    real_parts.append(real_part)
    t += h


plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(ylim = (-1, 1))
frame, = ax.plot([],[], lw = 3)
frame_list = []
for p in real_parts:
    frame, = ax.plot(x, p, color='cyan')
    frame_list.append([frame,])


anim = am.ArtistAnimation(fig, frame_list, interval = 20, blit = True)
anim.save('psiwave.mp4')
plt.show()