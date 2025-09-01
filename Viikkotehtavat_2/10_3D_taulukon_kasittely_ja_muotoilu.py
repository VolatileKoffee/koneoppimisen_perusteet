import numpy as np

if __name__=="__main__":
    array_a = np.random.randint(0,100,(2,3,4))
    print(array_a)

    print(f"Ensimmaisen dimension (depth) kerros:\n{array_a[0]}")
    
    array_a[0] = 0
    print(f"Vaihdetaan ensimmaisen tason arvot nolliin:\n{array_a}")

    array_a = array_a.reshape(6,4)
    print(f"Muutetaan taulukon muoto 6x4:\n{array_a}")

    print(f"Taulukon keskihajonta: {np.std(array_a)}")