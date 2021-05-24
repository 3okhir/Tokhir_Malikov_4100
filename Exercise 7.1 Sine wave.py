# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:19:13 2021

@author: tmali
"""

import sys
import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt
import Ex7_1mod as mod

if __name__ == "__main__":

    print(sys.argv[0])
    print("Argument list: ", str(sys.argv))


    
    def args():
        if len(sys.argv) == 2:
            N = int(sys.argv[1])
        pass


    
    N = 1000

    
    y1 = np.ones(N)

    
    y1[:N // 2] = 0

    
    swav = mod.dft(y1)

    
    saw = abs(swav)

   
    plt.title("Saw DFT Wave")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(saw[10:50])
    plt.show()

    X2 = fftpack.fft(saw)
    freqs2 = fftpack.fftfreq(len(saw))
    fig, ax = plt.subplots()
    ax.set_title('Saw Tooth Wave Coefficients')
    ax.stem(freqs2, np.abs(X2))
    ax.set_xlabel('Frequency in Hertz [Hz]')
    ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
    ax.set_xlim(-0.05, 0.05)
    plt.show()