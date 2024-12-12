def exercise2():
    temp = int(input("Please type in the temperature: "))
    if temp < 0:
        print("It's freezing!")
    if temp < 10:
        print("It's cold!")
    if temp < 20:
        print("It's cool!")
    print("stay safe!")


repeat = True
while repeat:
    exercise2()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
