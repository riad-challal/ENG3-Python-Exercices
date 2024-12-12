def exercise3():
    weekdays = ["Monday", "tuesday", "Wednesday", "Thursday", "Friday"]
    weekends = ["Saturday", "Sunday"]

    total_amount = float(input("Total amount: "))
    nb_item = int(input("Number of items: "))
    repeat = True
    discount = 0
    while (repeat):
        day = str(input("Day of the week: ")).capitalize()
        if day in weekdays:
            discount = 10
            repeat = False
        elif day in weekends:
            discount = 20
            repeat = False
        else:
            print("make sure to write the right weekday")
    if nb_item > 5:
        discount += 5
    final_price = (1 - discount / 100) * total_amount
    print(f"Total price after discount: {final_price}dinars")


repeat = True
while repeat:
    exercise3()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
