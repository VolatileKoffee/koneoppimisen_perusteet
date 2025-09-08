import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    fig, ax = plt.subplots(nrows=2, ncols=2)

    x = np.arange(0,2*np.pi,0.1)

    ax[0,0].set_title("sin(x)")
    ax[0,0].plot(x, np.sin(x), color="red")

    ax[0,1].set_title("cos(x)")
    ax[0,1].plot(x, np.cos(x), color="green")

    ax[1,0].set_title("sin(2x)")
    ax[1,0].plot(x, np.sin(2 * x), color="blue")

    ax[1,1].set_title("cos(2x)")
    ax[1,1].plot(x, np.cos(2 * x), color="orange")

    plt.tight_layout()
    plt.show()