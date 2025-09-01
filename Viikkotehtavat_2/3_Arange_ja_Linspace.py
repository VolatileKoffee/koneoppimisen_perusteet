import numpy as np

if __name__=="__main__":
    first_table = np.arange(0,20,2) # start, stop, step
    second_table = np.linspace(0,5,10) # start, stop, num of samples
    
    
    print(f"arange-taulukko: {first_table}")
    print(f"linspace-taulukko: {second_table}\n")

    print("arange kayttaa 'step' parametria arvojen etaisyyksien määrittelemiseen, kun taas linspacen parametri 'number of samples' maarittelee naytteiden tai arvojen kokonaismaaran annetulle välille.")