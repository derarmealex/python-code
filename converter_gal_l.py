repeat = True
while repeat:
    gal = input("Enter gallons:\n")
    if gal.isnumeric():
        print(gal, "gal is", round(int(gal)/0.26, 2), "l", "\n")
        repeat = False
        another_gal = input("Do you have another value for measure? y/n\n")
        if another_gal == "y":
            repeat = True
        elif another_gal == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in gal:
        print(gal, "gal is", round(float(gal)/0.26, 2), "l", "\n")
        repeat = False
        another_gal = input("Do you have another value for measure? y/n\n")
        if another_gal == "y":
            repeat = True
        elif another_gal == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")