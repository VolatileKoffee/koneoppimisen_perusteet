import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    x = np.random.normal(5.0, 1.0, 100000) # mean, std, values
    
    plt.hist(x, 20, color="orange", alpha=0.75) # values, pillars
    plt.show()