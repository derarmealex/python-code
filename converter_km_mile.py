repeat = True
while repeat:
    km = input("Enter kilometres:\n")
    if km.isnumeric():
        print(km, "km is", round(int(km)*0.62, 2), "mile", "\n")
        repeat = False
        another_km = input("Do you have another value for measure? y/n\n")
        if another_km == "y":
            repeat = True
        elif another_km == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in km:
        print(km, "km is", round(float(km)*0.62, 2), "mile", "\n")
        repeat = False
        another_km = input("Do you have another value for measure? y/n\n")
        if another_km == "y":
            repeat = True
        elif another_km == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")