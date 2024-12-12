def exercise6():
    price = float(input("Please type in a price: "))
    dinars = int(price)
    centimes = int(round((price - dinars) * 100))
    print(f"Dinars: {dinars}")
    print(f"Centimes:{centimes}")


repeat = True
while repeat:
    exercise6()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
