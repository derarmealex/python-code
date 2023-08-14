while True:
    gal = input("Enter gallons:\n")
    if gal.isnumeric():
        print(gal, "gal is", round(int(gal)/0.26, 2), "l", "\n")
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
    elif "." in gal:
        print(gal, "gal is", round(float(gal)/0.26, 2), "l", "\n")
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
