while True:
    mile = input("Enter miles:\n")
    if mile.isnumeric():
        print(mile, "mile is", round(int(mile)/0.62, 2), "km", "\n")
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
    elif "." in mile:
        print(mile, "mile is", round(float(mile)/0.62, 2), "km", "\n")
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