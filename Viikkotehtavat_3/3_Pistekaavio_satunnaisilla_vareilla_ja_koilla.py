import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    x = np.random.randint(0,50,50)
    y = np.random.randint(0,50,50)

    colors = np.arange(0,500,10) # must be same length as x and y
    sizes = np.arange(0,500,10)
    
    plt.scatter(x,y, c=colors, s=sizes, cmap="viridis") # 'c' instead of 'color' to color each dot
    plt.colorbar()
    plt.show()