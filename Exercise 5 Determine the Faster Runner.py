def exercise5():
    print("runner1: ")
    run1_name = input("Name: ")
    run1_time = float(input("Time (in seconds): "))
    print("runner2: ")
    run2_name = input("Name: ")
    run2_time = float(input("Time (in seconds): "))
    if run1_time > run2_time:
        print(f"The faster runner is {run2_name}")
    elif run1_time < run2_time:
        print(f"The faster runner is {run1_name}")
    else:
        print(f"{run1_name} and {run2_name} have the same time")


repeat = True
while repeat:
    exercise5()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
