import numpy as np 

if __name__=="__main__":
    og_array = np.ones((2,3), dtype=int)
    print(f"Alkuperainen taulukko:\n {og_array}")

    og_array[0,:] = 5
    print(f"Vaihdetaan 1. rivin arvot luvuksi 5:\n {og_array}")

    new_row = np.array([7,8,9])
    new_array = np.vstack((og_array, new_row))
    print(f"Lisataan rivi [7,8,9] np.vstack-komennolla:\n {new_array}")

    new_col_1d = np.array([10,11,12])
    new_col_2d = new_col_1d.reshape(-1,1) # numpy calculates rows with -1, 1 cols
    final_arr = np.hstack((new_array, new_col_2d))
    print(f"Lisataan sarake [10,11,12] np-hstack-komennolla:\n {final_arr}")