import numpy as np

if __name__=="__main__":
    value_arr = np.random.randint(0,10,(3,4))
    print(f"Satunnaisia kokonaislukuja valilta 1-10 muodossa 3x4:\n{value_arr}")

    print(f"Keskiarvo sarakkeittain: {np.mean(value_arr,axis=0)}")
    print(f"Kunkin rivin maksimi: {np.max(value_arr, axis=1)}")
    print(f"Koko taulukon arvojen summa: {np.sum(value_arr)}")