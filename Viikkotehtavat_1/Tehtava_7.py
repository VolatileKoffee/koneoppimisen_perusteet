def sales_volume():
    week_report = {}
    while len(week_report) < 7:
        weekday = input("Lisaa myyntipaiva: ")
        if weekday == "":
            print("Myyntipaivaa ei lisatty. Yrita uudelleen.")
            break
        elif weekday in week_report:
            print("Myyntipaiva jo taulukossa! Lisaa toinen.")
            continue
        else:
            try:
                weekday_sale = int(input("Lisaa myyntipaivan myynti euroissa: "))

            except ValueError:
                print("Virhe: ValueError! Jatketaan..")
                continue

        week_report[weekday]=weekday_sale
    
    return week_report 

def calculations(dict):
    total_sales = 0
    avg_sales = 0.0
    most_profitable_days_list = []
    max_profits = max(dict.values())

    for weekday, sales_volume in dict.items(): # total sales
        total_sales += sales_volume
    
    avg_sales = total_sales / len(dict)        # average sales
    
    for weekday in dict:                       # day with most profits
        if dict[weekday] == max_profits:
            most_profitable_days_list.append(weekday)

    print(f"Kokonaismyynti: {total_sales}")
    print(f"Keskimaarainen myynti: {avg_sales:.2f}")
    print(f"Tuottoisin myyntipaiva: ",end="") # end="" disables newline
    print(*most_profitable_days_list)

if __name__=="__main__":
    while True:
        user_input = int(input("Valitse toiminto: 1 - Aloita tai 0 - Lopeta: "))
        match user_input:
            case 1:
                print("Aloitetaan!")
                received_week_report = sales_volume()
                print(received_week_report)
                calculations(received_week_report)
            case 0:
                print("Hei hei, lopetetaan.")
                break
            case default:
                print("Ei sallittu toiminto.")