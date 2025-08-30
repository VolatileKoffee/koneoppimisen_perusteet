def products():
    product_list = []

    while len(product_list) < 5:
        product = input("Lisaa tuote: ")
        if product == "":
            print("Tuotteen nimi ei kelpaa!")
        else:
            product_list.append(product)
    return product_list

def print_products(list):
    print("Tuotelista: ")
    for (i,product) in enumerate(list, start=1):
        print(f"{i} {product}")

if __name__ == "__main__":
    while True:
        user_input = input("Valitse toiminto: aloita (a) tai lopeta (l): ")
        match user_input:
            case "a":
                print("Aloitetaan!")
                received_products = products()
                print_products(received_products)
            case "l":
                print("Lopetetaan!")
                break
            case default:
                print("Tuntematon komento..")
                