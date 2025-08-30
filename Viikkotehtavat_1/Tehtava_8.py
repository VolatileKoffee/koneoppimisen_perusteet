import random

def special_offers():
    product_list = ["maito", "leipa", "keksi", "kahavi", "kaakao", "pulla", "kakku", "piirakka", "donitsi", "patonki"]
    print(f"Alustavat erikoistuotteet ovat: {product_list}")
    while True:
        user_input = input("Haluatko lisätä arvattavia tuotteita? k/e: ")
        if user_input == "k":
            added_item = input("Kirjoita lisattava tuote: ")
            if added_item in product_list:
                print("Tuote jo listassa! Lisaa toinen.")
                continue
            else:
                product_list.append(added_item.lower())
                print("Lisatty!")
            continue
        elif user_input == "e":
            print("Edetaan peliin!")
            break
        else:
            print("Ei sallittu toiminto.")
            continue
    user_guess_func(product_list) # tämä aloittaa pelin

def user_guess_func(list):

    index_of_special_offer = random.randint(0,len(list)) # arvotaan erikoistuote listan indeksillä
    print(f"Arvattavat erikoistuotteet ovat: {list}")

    while True:
        user_input = input("Arvaa erikoistuote: ")

        # selvitetään indeksi, jos tuote on listassa
        if user_input in list:
            index_of_user_input = list.index(user_input)

            if index_of_user_input == index_of_special_offer:
                print("Oikein arvattu!")
                print(f"Erikoistuote on {list[index_of_special_offer]}")
                break
            elif index_of_user_input < index_of_special_offer:
                print("Oikea tuote on arvatun oikealla puolella..")
                continue
            elif index_of_user_input > index_of_special_offer:
                print("Oikea tuote on arvatun vasemmalla puolella..")
                continue
        else:
            print("Ei listassa..")
            continue

if __name__=="__main__":
    special_offers()