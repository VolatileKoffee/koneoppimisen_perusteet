def ask_user_review():
    user_reviews = []
    while True:
        review = input("Kirjoita lyhyt arvostelu tai jata tyhjaksi tuloksia varten: ")
        if review == "":
            print("Lopetetaan...")
            break
        else:
            user_reviews.append(review)

    return user_reviews

def modifying_reviews(list):
    total_A_chars = 0

    # printing all reviews in uppercase
    for review in list:
        print(review.upper())

    # checking how many A-character does reviews have
        total_A_chars += (review.count("a") + review.count("A")) # or index(), but requires error handling
    print(f"A-kirjaimia esiintyi yhteensa: {total_A_chars} kappaletta.")

if __name__=="__main__":
    while True:
        user_choice = input("Aloita ohjelma (a) tai lopeta (l): ")
        if user_choice == "a":
            print("Aloitetaan!")
            received_review_list = ask_user_review()
            modifying_reviews(received_review_list)
        elif user_choice == "l":
            print("Lopetetaan..")
            break
        else:
            print("Tuntematon komento..")