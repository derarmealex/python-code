while True:
    l = input("Enter liters:\n")
    if l.isnumeric():
        print(l, "l is", round(int(l)*0.26, 2), "gal", "\n")
        while True:
            another_choise = input("Do you have another value for measure? y/n\n")
            if another_choise == "y":
                break
            elif another_choise == "n":
                print("\nSee ya again!")
                input("\nPress any key")
                exit()
            else:
                print("\nPress 'y' or 'n'".upper())
    elif "." in l:
        print(l, "l is", round(float(l)*0.26, 2), "gal", "\n")
        while True:
            another_choise = input("Do you have another value for measure? y/n\n")
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