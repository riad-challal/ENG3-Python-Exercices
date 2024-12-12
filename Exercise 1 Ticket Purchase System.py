def exercise1():
    name = input("Please enter your name: ")
    if name != "VIP":
        nb_ticket = int(input("How many tickets would you like to buy? "))
        total_cost = nb_ticket * 15.5
        print(f"The total cost is {total_cost}")
    else:
        print("Enjoy the show for free!")


repeat = True
while repeat:
    exercise1()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
