import numpy as np

if __name__=="__main__":
    a = np.arange(10)
    print(f"Alkuperainen taulukko a: {a}")

    b = a[2:6]
    b[0] = 100
    print(f"Taulukko b: {b}")

    print(f"Taulukon a tarkistus: {a}\nHuomaa, etta taulukon b 'view' muutti alkuperaisen taulukon a arvoa!")

    c = a[2:6].copy()
    c[0] = 200

    print(f"Taulukko c: {c}\nHuomaa, ettei 'copy' ei tehnyt muutoksia a-taulukkoon!")
    print(f"Taulukko atarkistus: {a}")

    print(f"Copy tekee uuden itsenaisen taulukkokopion omalla muistillaan. View taas jakaa saman muisti alkuperaisen taulukon kanssa. Taman vuoksi view-taulukkomuutokset nakyvat myos alkuperaisessa taulukossa.")