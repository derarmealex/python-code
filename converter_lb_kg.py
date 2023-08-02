repeat = True
while repeat:
    Lb = input("Enter libres:\n")
    if Lb.isnumeric():
        print(Lb, "lb is", round(int(Lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_Lb = input("Do you have another value for measure? y/n\n")
        if another_Lb == "y":
            repeat = True
        elif another_Lb == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in Lb:
        print(Lb, "lb is", round(float(Lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_Lb = input("Do you have another value for measure? y/n\n")
        if another_Lb == "y":
            repeat = True
        elif another_Lb == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")