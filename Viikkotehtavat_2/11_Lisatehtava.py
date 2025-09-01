import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    height = 256
    width = 256
    rgb_array = np.zeros((height,width,3),dtype=np.uint8) # full black image
    print(rgb_array)

    # declare mid_row, mid_col

# Code template below was provided to us by school (STILL IN DEVELOPMENT)

# only red is valid in these!!!
rgb_array[0:mid_row, 0:mid_col,0] = [255,0,0] # red
rgb_array[0:mid_row, 0:mid_col,0] = [0,0,255] # blue
rgb_array[0:mid_row, 0:mid_col,0] = [0,255,0] # green
rgb_array[0:mid_row, 0:mid_col,0] = [128,128,128] # gray

# Näytä kuva
plt.figure()
plt.imshow(rgb_array/255)
