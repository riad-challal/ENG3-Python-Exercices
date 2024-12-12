def exercise9():
    cities_list = []
    while (True):
        city = str(input("give the name of a city: "))
        if city != "stop":
            cities_list.append(city)
        else:
            break
    cities_list = sorted(cities_list, key=len, reverse=True)
    for city in cities_list:
        nb_letters = len(city)
        population = nb_letters * 1000000
        print(f"the city {city} has {nb_letters} letters, so its population is {population}")


repeat = True
while repeat:
    exercise9()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
