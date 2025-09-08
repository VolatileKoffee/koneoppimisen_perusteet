import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    x = np.arange(0,2 * np.pi,0.01)
    
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="Sine-wave", linestyle="dashed")
    plt.plot(x, y2, label="Cosine-wave", linestyle="dotted")
    plt.legend()
    plt.title("Sine and Cosine wave graphs")
    plt.xlabel("x-values")
    plt.ylabel("y-values")
    plt.grid()
    # plt.axis("equal")
    plt.show()