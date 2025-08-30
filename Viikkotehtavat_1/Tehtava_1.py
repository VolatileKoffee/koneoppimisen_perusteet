def userCheck():
    while True:
        user = input("Anna rooli (asiakas/tyontekija) tai kirjoita loppu: ")
        
        #convert whole string to lowercase
        lowercaseUser = user.lower()
        if lowercaseUser == "asiakas":
            print("Tervetuloa kahvilaan!")
        elif lowercaseUser == "tyontekija":
            print("Tervetuloa töihin!")
        elif lowercaseUser == "loppu":
            print("Tunnistus paattyy..")
            break
        else:
            print("Tuntematon rooli.")
            continue

if __name__ == "__main__":
    while True:
        user_input = input("Suorita tunnistus? k/e: ")
        match user_input:
            case "k":
                print("Aloitetaan...")
                userCheck()
            case "e":
                print("Lopetetaan...")
                break
            case default:
                print("Tuntematon komento...")
                