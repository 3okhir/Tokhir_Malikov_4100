# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:00:59 2021

@author: tmali
"""


import numpy

import pylab

import random

  

# defining the number of steps

n = 1000000

x = numpy.zeros(n)

y = numpy.zeros(n)

  

for i in range(1, n):

    val = random.randint(1, 4)

    if val == 1:

        x[i] = x[i - 1] + 1

        y[i] = y[i - 1]

    elif val == 2:

        x[i] = x[i - 1] - 1

        y[i] = y[i - 1]

    elif val == 3:

        x[i] = x[i - 1]

        y[i] = y[i - 1] + 1

    else:

        x[i] = x[i - 1]

        y[i] = y[i - 1] - 1

      

pylab.title("Random Walk ($n = " + str(n) + "$ steps)")

pylab.plot(x, y)

pylab.savefig("rand_walk"+str(n)+".png",bbox_inches="tight",dpi=600)

pylab.show()