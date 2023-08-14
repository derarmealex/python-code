while True:
    kg = input("Enter kilograms:\n")
    if kg.isnumeric():
        print(kg, "kg is", round(int(kg)*2.2, 2), "lb", "\n")
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
    elif "." in kg:
        print(kg, "kg is", round(float(kg)*2.2, 2), "lb", "\n")
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
