while True:
    km = input("Enter kilometres:\n")
    if km.isnumeric():
        print(km, "km is", round(int(km)*0.62, 2), "mile", "\n")
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
    elif "." in km:
        print(km, "km is", round(float(km)*0.62, 2), "mile", "\n")
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
