def multiplication_table():
    print("Kahvien pakkauskoot riveissä 1-5kg ja hinnat sarakkeissa 10-14€/kg")
    
    for i in range(1,6):
        print()
        print(f"{i} kg", end="\t")
        
        for j in range(10,15):
            print(f"{i*j} €", end="\t")
    print("\n")

def user_choice():
    while True:
        choice = int(input("Valitse toiminto (1) Nayta taulukko tai (0) Lopetus: "))
        if choice == 1:
            multiplication_table()
        elif choice == 0:
            print("Hei hei.")
            break
        else:
            print("Ei sallittu toiminto.")

if __name__=="__main__":
    user_choice()