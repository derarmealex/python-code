from re import findall
while True:
    km = input("Enter kilometres: ").strip()
    if findall('[^.\d]', km) or km == '0' or km == '.' or km in '':
        print("Enter a correct number!")
    else:
        print(km, "km is", round(float(km) * 0.62, 2), "mile", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
