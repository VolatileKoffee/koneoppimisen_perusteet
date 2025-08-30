import random

def cafe_temperatures():
    day_list = ["ma", "ti", "ke", "to", "pe", "la", "su"]
    temp_list = []
    while len(temp_list) < 7:
        measured_temp = random.uniform(19.0,25.0)
        temp_list.append(round(measured_temp, 1))

    print(f"Mitatut lampotilat ma-su: {temp_list}")
    return day_list, temp_list

def print_information(days,temps):
    coldest_days = []
    cold_day = min(temps)
    cold_day_index = temps.index(cold_day)

    warmest_days = []
    warm_day = max(temps)
    warm_day_index = temps.index(warm_day)

    avg_temp = sum(temps) / len(temps)
    print(f"Keskimaarainen lampotila {avg_temp:.1f}C")
    
    for temp in temps:
        if temp == cold_day:
            coldest_days.append(temp)
        elif temp == warm_day:
            warmest_days.append(temp)
    print(f"Kylmin tai kylmimmat paivat {days[cold_day_index]}",end=" ")
    print(*coldest_days, end=" ")
    print("celsiusasteta.")
    print(f"Lampimin tai lampimimmat paivat {days[warm_day_index]}",end=" ")
    print(*warmest_days,end=" ")
    print("celsiusastetta.")

def user_choice():
    while True:
        user_choice = int(input("Valitse toiminto (1) Arvo lampotilat tai (0) Lopetus: "))
        match user_choice:
            case 1:
                day_list, temp_list = cafe_temperatures()
                print_information(day_list, temp_list)
            case 0:
                print("Goodbye.")
                break
            case default:
                print("Ei sallittu toiminto.")

if __name__=="__main__":
    user_choice()