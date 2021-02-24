# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:32:33 2021

@author: tmali
"""

import math 

# Take relative speed from user
v = float(input("Enter Relative Speed (as a fraction of the speed of light c): "))

# Take distance of spaceship from another planet
x = float(input("Enter distance of spaceship from another planet in lightyears: "))


t0 = x / v # Compute the time in years in the rest frame of an observer on Earth


print("\nTime in years (In the rest frame of an observer on Earth): {:.2f}".format(t0), "Years") # Print computed time in years in the rest frame of an observer on Earth


ts = (t0*(math.sqrt(1 - v**2))) # Compute time in years as perceived by a passenger on board the ship

print("\nTime in years (As perceived by a passenger on board the ship): {:.2f}".format(ts), "Years") # Print time in years as perceived by a passenger on board the ship