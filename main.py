import random

print("Witaj w zgadywance")

top_of_range = input("Podaj gorna granice zakresu liczb\n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Wybrana liczba jest za mała. Nastepnym razem wybierz cos wiekszego od 0.")
        quit()
else:
    print("To nie liczba. Nastepnym razem wybierz jakis numer.")
    quit()
r = random.randint(0,top_of_range)
liczba_prob = 0
# print(r)

while True:
    liczba_prob += 1
    user_guess = input("Zgaduj! ^^\n")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Zakres zaczyna sie od 1.")
            continue

    else:
        print("To nie liczba. Nastepnym razem wybierz jakis numer.")
        continue

    if user_guess == r:
        print("Zgadles!")
        print(f"Liczba Twoich podejsc to: {liczba_prob}")
        break
    elif user_guess > r:
        print("Wskazales za duza liczbe")
    else:
        print("Wskazales za mala liczbe")