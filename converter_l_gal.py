repeat = True
while repeat:
    l = input("Enter liters:\n")
    if l.isnumeric():
        print(l, "l is", round(int(l)*0.26, 2), "gal", "\n")
        repeat = False
        another_l = input("Do you have another value for measure? y/n\n")
        if another_l == "y":
            repeat = True
        elif another_l == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in l:
        print(l, "l is", round(float(l)*0.26, 2), "gal", "\n")
        repeat = False
        another_l = input("Do you have another value for measure? y/n\n")
        if another_l == "y":
            repeat = True
        elif another_l == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")