import numpy as np

def print_first_table():
    random_arr = np.random.rand(8,)
    print(random_arr)
    random_arr_mem_usage = random_arr.size * random_arr.itemsize # .size = n of elements in arr, .itemsize = size of element in bytes
    print(f"random_arr's mem usage in bytes {random_arr_mem_usage}")

def print_second_table():
    empty_arr = np.empty((4,4))
    print(empty_arr)
    empty_arr_mem_usage = empty_arr.size * empty_arr.itemsize # .size = n of elements in arr, .itemsize = size of element in bytes
    print(f"empty_arr's mem usage in bytes {empty_arr_mem_usage}")

    # Numpy.empty-taulukon käyttäminen voi olla nopeaa, mutta sen sisältö vaihtuu satunnaisesti 
    # muistin tilan mukaan: se voi olla täysin tyhjä, siltä väliltä tai täynnä suuria arvoja.
    # Tyhjän listan täyttämättä jättäminen vie myös paljon muistia!

if __name__=="__main__":
    print_first_table()
    print_second_table()