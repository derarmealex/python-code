repeat = True
while repeat:
    lb = input("Enter libres:\n")
    if lb.isnumeric():
        print(lb, "lb is", round(int(lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_lb = input("Do you have another value for measure? y/n\n")
        if another_lb == "y":
            repeat = True
        elif another_lb == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in lb:
        print(lb, "lb is", round(float(lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_lb = input("Do you have another value for measure? y/n\n")
        if another_lb == "y":
            repeat = True
        elif another_lb == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")
