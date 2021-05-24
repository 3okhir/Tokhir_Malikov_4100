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

    
    y = np.linspace(0, 3, N)

    
    sqwav = mod.Sqrwav(y)

    # sqwav points plotted
    plt.title("Square Wave")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(y, sqwav)
    plt.show()

    X1 = fftpack.fft(sqwav)
    freqs1 = fftpack.fftfreq(len(sqwav))
    fig, ax = plt.subplots()
    ax.set_title('Square Wave Coefficients')
    ax.stem(freqs1, np.abs(X1))
    ax.set_xlabel('[Hz]')
    ax.set_ylabel('(Spectrum) Magnitude')
    ax.set_xlim(-0.05, 0.05)
    plt.show()