import numpy as np

def print_tables():
    print("Ensimmainen taulukko:")
    one_d_table = np.ones(10, dtype=int)
    print(one_d_table)
    print(f"1-ulotteisen taulukon muoto: {one_d_table.shape}, tietotyyppi: {one_d_table.dtype}, dimensiot: {one_d_table.ndim} ja alkiot: {one_d_table.size}\n")

    print("Toinen taulukko:")
    two_d_table = np.zeros((5,5), dtype=int)
    print(two_d_table)
    print(f"2-ulotteisen taulukon muoto: {two_d_table.shape}, tietotyyppi: {two_d_table.dtype}, dimensiot: {two_d_table.ndim} ja alkiot: {two_d_table.size}\n")

    print("Kolmas taulukko:")
    three_d_table = np.ones((2,3,4), dtype=int)
    print(three_d_table)
    print(f"3-ulotteisen taulukon muoto: {three_d_table.shape}, tietotyyppi: {three_d_table.dtype}, dimensiot: {three_d_table.ndim} ja alkiot: {three_d_table.size}\n")


if __name__=="__main__":
    print_tables()