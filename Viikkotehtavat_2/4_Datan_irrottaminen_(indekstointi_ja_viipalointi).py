import numpy as np

if __name__=="__main__":
    num_table = np.arange(10,20)
    print(f"Alkuperainen taulukko: {num_table}")
    indices = [2, 4, 6]
    print(f"Taulukon 3., 5. ja 7. alkio: {num_table[indices]}")
    print(f"Taulukon parilliset indeksit: {num_table[::2]}")
    print(f"Viimeiset 4 arvoa kaanteisesti: {num_table[-4:][::-1]}") # select last 4 & flip whole arr