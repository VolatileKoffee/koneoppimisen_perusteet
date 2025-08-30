
def special_offer():
    offer_tuple = ("Banaani",1.80)
    
    while True:
        user_choice = input(f"Haluatko ostaa paivan tarjouksen, {offer_tuple[0]} {offer_tuple[1]}€ ? (kylla/ei): ")
        
        if user_choice == "kylla":
            print("Lisatty ostoskoriin.")
            break
        elif user_choice == "ei":
            print("Ei lisatty.")
            break
        else:
            print("En ymmartanyt, yrita uudelleen.")

if __name__=="__main__":
    while True:
        user_input = int(input("Kirjoita 1 aloittaaksesi tai 0 lopettaaksesi: "))
        match user_input:
            case 1:
                special_offer()
            case 0:
                print("Lopetetaan. Hei hei!")
                break
            case default:
                print("Tuntematon komento..")