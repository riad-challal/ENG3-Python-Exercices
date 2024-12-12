def exercise8():
    print("**Input:**")
    nb = int(input("Number: "))
    print("**Output:**")
    if nb % 3 == 0 and nb % 5 == 0:
        print("FizzBuzz")
    elif nb % 3 == 0:
        print("Fizz")
    elif nb % 5 == 0:
        print("Buzz")


repeat = True
while repeat:
    exercise8()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
