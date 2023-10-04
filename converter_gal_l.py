from re import findall
while True:
    gal = input("Enter gallons: ").strip()
    if findall('[^0-9.]', gal) or gal == '0' or gal == '.' or gal in '':
        print("Enter a correct number!")
    else:
        print(gal, "gal is", round(float(gal) / 0.26, 2), "lt", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                exit()
