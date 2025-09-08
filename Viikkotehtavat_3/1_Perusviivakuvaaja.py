import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    # Luo numpy-array, which includes values 0–10 (with 0.1 step).
    x = np.arange(0,10,0.1)
    print(f"Original arr x: {x}")

    function_y = np.sin(x)
    
    # Draw function y = sin(x)
    plt.plot(function_y)
    plt.title("Function y = sin(x)")
    plt.xlabel("x-values")
    plt.ylabel("y-values")
    plt.grid()
    plt.show()
    # Lisää otsikko, x- ja y-akselin nimet sekä ruudukko (grid).