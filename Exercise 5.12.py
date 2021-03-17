# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:15:56 2021

@author: tmali
"""

from scipy import * #The scipy module is used to have integration operation

import numpy as np

from scipy.integrate import quad #command imports quad function which is used for single integration in python

def integrand(x): #defines x as an integrand for the integral operation

    output = x**3/(exp(x)-1) #stores the function in variable output which is required to be integrated

    return output

solution = quad(integrand,0,np.inf) #calculates the integrals within the specified limits, that is 0 and infinity

print (solution)
