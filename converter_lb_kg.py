from re import findall
while True:
    lb = input("Enter libres:\n").strip()
    if findall('[^.\d]', lb) or lb == '.' or lb == '':
        print("Wrong value, enter a number".upper())
    else:
        print(lb, "lb is", round(float(lb) / 2.2, 2), "kg", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
