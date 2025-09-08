import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    
    x = np.array(["A", "B", "C", "D"])
    y = np.random.randint(1,11,4)

    fig, ax = plt.subplots()
    bars = ax.bar(x,y)
    ax.set_title("Bar graph")
    ax.set_xlabel("Categories (x)")
    ax.set_ylabel("Values (y)")
    # ax.text() # old and requires for-loop
    ax.bar_label(bars) # newer option for ax.text()
    plt.show()