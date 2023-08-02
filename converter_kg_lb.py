repeat = True
while repeat:
    kg = input("Enter kilograms:\n")
    if kg.isnumeric():
        print(kg, "kg is", round(int(kg)*2.2, 2), "lb", "\n")
        repeat = False
        another_kg = input("Do you have another value for measure? y/n\n")
        if another_kg == "y":
            repeat = True
        elif another_kg == "n":
            print("See ya again")
            input()
        else:
            pass
    elif "." in kg:
        print(kg, "kg is", round(float(kg)*2.2, 2), "lb", "\n")
        repeat = False
        another_kg = input("Do you have another value for measure? y/n\n")
        if another_kg == "y":
            repeat = True
        elif another_kg == "n":
            print("See ya again")
            input()
        else:
            pass
    else:
        print("Wrong value, enter a number")