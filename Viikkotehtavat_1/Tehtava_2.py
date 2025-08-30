
def tempCheck():
        try:
            temp = float(input("Anna lampotila celius-asteina: "))

            if temp <= 10.0:
                print("Mainosta kuumia juomia.")
            elif (temp > 10.0 and temp < 20.0):
                print("Mainosta sekä kuumia että kylmiä juomia.")
            elif temp >= 20.0:
                print("Mainosta kylmiä juomia.")
        except ValueError:
            print("Virhe: ei numero!")

if __name__ == "__main__":
    while True:
        user_input = input("Mitataanko lampotila? k/e: ")
        match user_input:
            case "k":
                print("Aloitetaan!")
                tempCheck()
            case "e":
                print("Lopetetaan.")
                break
            case default:
                print("Tuntematon komento.")