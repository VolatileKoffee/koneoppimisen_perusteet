import numpy as np

if __name__=="__main__":
    original_array = np.random.randint(5,6,(3,3)) # tai np.full((3,3), 5)
    print(f"Alkuperainen taulukko:\n{original_array}")

    small_arr = np.arange(1,4,1)
    result = original_array + small_arr # 1d array to 2d array
    print(f"Lisataan taulukko {small_arr} 2d taulukkoon broadcastingilla:\n{result}")

    multiplied_by_2 = result * 2 # broadcasting
    print(f"Kerrotaan koko taulukko kahdella:\n{multiplied_by_2}")

    print(f"Mita broadcasting tekee rivin lisaamisessa:\nBroadcastingissa Numpy laajentaa 1d taulukkoa 2d taulukon rivien perusteella suorittaakseen alkiokohtaisen yhteenlaskun.\n")