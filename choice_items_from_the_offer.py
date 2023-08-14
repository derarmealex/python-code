fruits = {"apple": 0, "banana": 0, "lemon": 0, "pomerange": 0}
print("Avialable fruits:", ", ".join(fruits), "\n")
while True:
    choise = input("Choose from available fruits: ").lower()
    if choise in fruits:
        print("Great, this fruit is in offer")
        fruits[choise] += 1
        while True:
            another_choise = input("\nIf you like another fruit to choise, press 'y'\nFor seeing your basket, press 'b'\nTo finish shopping press 'n'\n")
            if another_choise == "y":
                break
            elif another_choise == "b":
                print("\nHere is your basket: ", ", ".join([f"{key}: {value}" for key, value in fruits.items()]))
            elif another_choise == "n":
                print("\nSee ya again!")
                print("Here is your basket: ", ", ".join([f"{key}: {value}" for key, value in fruits.items()]))
                input("\nPress any key")
                exit()
            else:
                print("\nPress 'y', 'n' or 'b'".upper())
    else:
        print("\nFruit is not in offer".upper())
