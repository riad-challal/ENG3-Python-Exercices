def exercise0():
    nbp = int(input('How many people need a ride? '))
    npt = int(input('How many people fit in one taxi? '))
    if nbp % npt != 0:
        number_taxi = nbp // npt + 1
    else:
        number_taxi = nbp // npt
    print(f"Number of taxis needed: {number_taxi}")


repeat = True
while repeat:
    exercise0()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
