def exercise4():
    age1 = int(input("Please type in the age of the first person: "))
    age2 = int(input("Please type in the age of the second person:"))
    if age1 != age2:
        print(f"The older age is: {max(age1, age2)}")
    # if age1>age2:
    #    print(f"The older age is: {age1}")
    # elif age1<age2:
    #   print(f"The older age is: {age2}")
    else:
        print("Both people are the same age!")


repeat = True
while repeat:
    exercise4()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
