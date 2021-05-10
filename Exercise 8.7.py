# -*- coding: utf-8 -*-
"""
Created on Sun May 09 10:39:26 2021

@author: tmali
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


g = 9.81
#kg
m = 1
#radius 
R = 0.08
#degrees
theta = np.radians(30)
# m/s
vi = 100
# kg per meter
rho = 1.22
#coefficient of drag
C = 0.47
ti, tf = 0, 10
N = 100
h = 0.1


def velocity(r,t,m):
    c = np.pi * R**2 * C * rho/(2*m)
    vx = r[1]
    vy = r[3]
    v = np.sqrt(vx**2 + vy**2) 
    dvx = v * vx * -c
    dvy = (v * vy * -c) - g 
    return np.array([vx, dvx, vy, dvy], float)

time = np.arange(ti,tf,h)

def traject(m):
    xs = []
    ys = []
    ts = []
    vi_x = vi * np.cos(theta)
    vi_y = vi * np.sin(theta)
    r = np.array([0, vi_x, 0, vi_y], float) 
    for t in time:
        k1 = h * velocity(r, t, m)
        k2 = h * velocity(r + 0.5 * k1, t + 0.5 * h, m)
        k3 = h * velocity(r + 0.5 * k2, t + 0.5 * h, m)
        k4 = h * velocity(r + k3, t + h, m)
        r += (k1 + 2 * k2 + 2 * k3 + k4)/6
        xs.append(r[0])
        ys.append(r[2])
        ts.append(t)
        #print(xs,ys)
        if r[2] <= 0:
            break
    return xs, ys, ts

x,y, time = traject(1)
x1,y1, time = traject(2)
x2, y2, time = traject(3)

plt.plot(x,y, 'g')
plt.plot(x1,y1, 'b')
plt.plot(x2,y2, 'r')
plt.show()


trace1 = go.Scatter(
    x=x,
    y=y,
    name = 'm1',
    mode='markers',
    
)
trace2 = go.Scatter(
    x=x1,
    y=y1,
    name = 'm2',
    mode='markers'
)
trace3 = go.Scatter(
    x=x2,
    y=y2,
    name = 'm5',
    mode='markers'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    yaxis=dict(
        domain=[0, 1],
    ),
    legend=dict(
        traceorder="normal"
    ),
    yaxis2=dict(
        domain=[0, 1],       
    ),
    yaxis3=dict(
        domain=[0, 1],
    ),
    
)

fig = go.Figure(data=data, layout=layout)
fig.write_html('cannonball2.html')
fig.show()