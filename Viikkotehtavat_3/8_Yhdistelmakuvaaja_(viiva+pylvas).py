import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    x = np.arange(1,13)
    y1 = np.random.randint(100,1000,12) # sales volume in €
    y2 = np.full_like(x, y1.mean(), dtype=float) # mean of sales volume
    
    fig, ax1 = plt.subplots()
    
    ax1_color = "orange"
    ax1.set_ylabel("Sales (€)",color=ax1_color)
    ax1.tick_params(axis="y", labelcolor=ax1_color)
    bars = ax1.bar(x,y1, alpha=0.75, color=ax1_color, label="Sales volume in €")
    ax1.bar_label(bars)
    
    ax2 = ax1.twinx() # same x, different y

    ax2_color = "blue"
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Mean",color=ax2_color)
    ax2.tick_params(axis="y", labelcolor=ax2_color)
    # ax2.axhline(y2, linestyle="dashed", color=ax2_color, label="Sales volume mean") # simplified, no need for lines 7,17,24
    ax2.plot(x, y2, color=ax2_color, label="Sales volume mean")

    plt.title("Sales volume and volume mean")
    ax1.legend()
    ax2.legend()

    plt.show()