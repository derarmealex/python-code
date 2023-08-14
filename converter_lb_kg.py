while True:
    lb = input("Enter libres:\n")
    if lb.isnumeric():
        print(lb, "lb is", round(int(lb)/2.2, 2), "kg", "\n")
        while True:
            another_choise = input("Do you have another value to measure? y/n\n")
            if another_choise == "y":
                break
            elif another_choise == "n":
                print("\nSee ya again!")
                input("\nPress any key")
                exit()
            else:
                print("\nPress 'y' or 'n'".upper())
    elif "." in lb:
        print(lb, "lb is", round(float(lb)/2.2, 2), "kg", "\n")
        while True:
            another_choise = input("Do you have another value to measure? y/n\n")
            if another_choise == "y":
                break
            elif another_choise == "n":
                print("\nSee ya again!")
                input("\nPress any key")
                exit()
            else:
                print("\nPress 'y' or 'n'".upper())
    else:
        print("Wrong value, enter a number".upper())
