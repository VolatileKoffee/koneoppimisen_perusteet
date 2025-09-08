import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # sampling frequency
time = np.arange(0, 0.1, 1/fs)
amplitude = 1
if __name__=="__main__":
    fig, axs = plt.subplots(nrows=2, ncols=2)


    sine_100 = amplitude * np.sin(2*np.pi*100*time)
    sine_300 = (amplitude/3) * np.sin(2*np.pi*300*time)
    sine_500 = (amplitude/5) * np.sin(2*np.pi*500*time)

    sine_combi = sine_100 + sine_300 + sine_500

    axs[0,0].set_title("100 Hz, A=1")
    axs[0,0].plot(time, sine_100, color="red")
    axs[0,0].set_xlim(0,0.01) # zooming to 10ms
    
    axs[0,1].set_title("300 Hz, A=1/3")
    axs[0,1].plot(time, sine_300, color="green")
    axs[0,1].set_xlim(0, 0.01) # zooming to 10ms

    axs[1,0].set_title("500 Hz A=1/5")
    axs[1,0].plot(time, sine_500, color="blue")
    axs[1,0].set_xlim(0, 0.01) # zooming to 10ms

    axs[1,1].set_title("Sum of signals")
    axs[1,1].plot(time, sine_combi, color="orange")
    axs[1,1].set_xlim(0, 0.01) # zooming to 10ms

    plt.tight_layout()
    plt.show()
