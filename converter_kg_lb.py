from re import findall
while True:
    kg = input("Enter kilograms: ").strip()
    if findall('[^.\d]', kg) or kg == '0' or kg == '.' or kg in '':
        print("Enter a correct number!")
    else:
        print(kg, "kg is", round(float(kg) * 2.2, 2), "lb", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
