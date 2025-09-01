import numpy as np

if __name__=="__main__":
    new_arr = np.arange(16)
    print(f"Alkuperainen muoto: {new_arr}")

    reshaped_arr = new_arr.reshape(4,4)
    print(f"Muodossa 4x4: \n{reshaped_arr}\nTama onnistuu, koska lukuja on tasainen maara.")

    reshaped_arr_again = reshaped_arr.reshape(2,8)
    print(f"Muodossa 2x8:\n{reshaped_arr_again}\nTassa sama juttu!")

    back_to_1d_arr = reshaped_arr_again.reshape(-1) # flattening 2d arr to 1d arr
    print(back_to_1d_arr)

    print("'reshape' ei toimi, jos taulukossa on eri maara muutettavia alkioita kuin muutoskomennossa.\nEsim 8 alkiota ei riita tassa: reshape(3,3) = 9 alkiota")