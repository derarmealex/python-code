repeat = True
while repeat:
    mile = input("Enter miles:\n")
    if mile.isnumeric():
        print(mile, "mile is", round(int(mile)/0.62, 2), "km", "\n")
        repeat = False
        another_mile = input("Do you have another value for measure? y/n\n")
        if another_mile == "y":
            repeat = True
        elif another_mile == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in mile:
        print(mile, "mile is", round(float(mile)/0.62, 2), "km", "\n")
        repeat = False
        another_mile = input("Do you have another value for measure? y/n\n")
        if another_mile == "y":
            repeat = True
        elif another_mile == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")