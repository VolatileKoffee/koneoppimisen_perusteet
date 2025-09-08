import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    x = np.arange(0,5)
    # print(x)
    y = np.exp(-x) * np.sin(2 * np.pi * x)
    
    fig, ax = plt.subplots()
    
    ax.plot(x,y,"ro--",label="y = e^(-x) * sin(2πx)")
    ax.set_title("title")
    ax.set_xlabel("x-values")
    ax.set_ylabel("y-values")
    ax.legend()
    ax.grid()

    plt.show()