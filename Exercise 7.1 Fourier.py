# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:36:50 2021

@author: tmali
"""

import sys
import os

if __name__ == "__main__":
    print(sys.argv[0]) 
    print("Argument list: ", str(sys.argv))


    def args():
        if len(sys.argv) == 2:
            a = int(sys.argv[1])
        else:
            print('enter:  1 for square wave, \t, 2 for saw tooth wave, \t, 3 for sine wave ')
            a = int(input("Enter a number: "))
        return a
    pass
    
    def select(a):

        print("you entered: ", a)

        if a == 1:

            os.system('python Ex7_SqarWave.py')

        elif a == 2:

            os.system('python Ex7_SawWave.py')

        elif a == 3:

            os.system('python Ex7_SineWave.py')
            
    select(args())