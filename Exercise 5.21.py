# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:28:57 2021

@author: tmali
"""

import numpy as np
import matplotlib.pyplot as plt

#This function exactly solves given a function, grid spacing and min error required
def solve(rho,error,hx,hy=-1):
   if hy==-1:
       hy=hx
   solution=np.zeros_like(rho)
   solution_temp=np.zeros_like(solution)
   solution_temp=solution
   while(1):
       solution_temp=iterate(solution,rho,hx,hy)
       error_temp=solution_temp-solution
       error_temp=np.abs(error_temp)
       solution=solution_temp
       if(np.amax(error_temp)<error):
           break

   return solution

#This function returns the next iteration of Jacobi iteration for poisson solver
def iterate(solution,rho,hx,hy):
   solved=np.zeros_like(rho)
   [lr,lc]=np.shape(rho)
   if lr!=1:
       solved[0,:]=solution[0,:]
       solved[lr-1,:]=solution[lr-1,:]
   if lc!=1:
       solved[:,0]=solution[:,0]
       solved[:,lc-1]=solution[:,lc-1]
  
   if lr==1:
       solved[0,1:lc-1]=(solution[0,0:(lc-2)]+solution[0,2:lc]-(hx**2)*rho[0,1:(lc-1)])/2
   elif lc==1:
       solved[1:lr-1,0]=(solution[0:(lr-2),0]+solution[2:lr,0]-(hy**2)*rho[1:(lr-1),0])/2
   else:
       solved[1:(lr-1),1:(lc-1)]=(((hx**2)*(solution[0:(lr-2),1:(lc-1)]+solution[2:lr,1:(lc-1)]-((hy**2)*rho[1:(lr-1),1:(lc-1)]/2)))+((hy**2)*(solution[1:(lr-1),0:(lc-2)]+solution[1:(lr-1),2:lc]-((hx**2)*rho[1:(lr-1),1:(lc-1)]/2))))/(2*((hx**2)+(hy**2)))

   return solved

#Charge distribution for first and second part
rho=np.zeros([100,100])
rho[45,50]=1
rho[55,50]=-1


#Charge distribution for third part
x1=np.linspace(-0.5,0.5,100)
x,y=np.meshgrid(x1,x1)
rho=100*np.sin(2*np.pi*x/0.1)*np.sin(2*np.pi*y/0.1)

#Potential(phi) is calculated using Jacobi iteration
phi=solve(rho,0.000001,0.01,0.02)


# Plotting the potential
plt.matshow(phi)
plt.colorbar()
plt.show()


#Plotting the electric field
Ex,Ey=np.gradient(phi)
E=np.sqrt(Ex**2+Ey**2)
plt.quiver(-Ey[::4,::4],Ex[::4,::4])
plt.show()