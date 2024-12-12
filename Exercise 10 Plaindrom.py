def exercise10():
    word = str(input("give us a word to check if its a palindrome "))
    j = 1
    palindrome = True
    for char in word:
        if char != word[-j]:
            palindrome = False
            break
        else:
            j += 1
        if j > len(word) / 2 + 1:
            break
    if palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")


repeat = True
while repeat:
    exercise10()
    rep = input("Press Q to quit  |  Any key to repeat: ").lower()
    if rep == "q":
        repeat = False
