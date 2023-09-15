from re import findall
while True:
    mile = input("Enter miles: ").strip()
    if findall('[^.\d]', mile) or mile == '0' or mile == '.' or mile in '':
        print("Enter a correct number!")
    else:
        print(mile, "mile is", round(float(mile) / 0.62, 2), "km", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
