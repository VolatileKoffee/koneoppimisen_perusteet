
def add_to_shopping_cart():
    shopping_cart = {} # where key = product, value = price
    while True:
        product_name = input("Anna tuotteen nimi: ")

        if (product_name == ""):
            print("Syöte on tyhjä. Lopetetaan...")
            break
        elif product_name in shopping_cart:
            print("Tuote jo ostoskorissa! Lisaa toinen.")
        else:
            while True:
                product_price = int(input("Anna tuotteen hinta: "))
                if product_price <= 0:
                    print("Virhe: hinta nolla tai negatiivinen. Yrita uudelleen.")

                else:
                    shopping_cart[product_name]=product_price
                    break
    return shopping_cart 

def print_cart(dict):
    total_value = 0
    print(f"Kaikki tuotteet:")

    for key, value in dict.items():
        total_value += value
        print(f"{key}")

    print(f"Yhteissumma: {total_value}")

if __name__ == "__main__":
    while True:
        user_input = int(input("Valitse toiminto: 1 - Aloita tai 0 - Lopeta: "))
        if user_input == 1:
            print("Aloitetaan!")
            returned_shopping_cart = add_to_shopping_cart()
            print_cart(returned_shopping_cart)
        elif user_input == 0:
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon komento..")