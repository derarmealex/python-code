import re
while True:
    kg = input("Enter kilograms:\n").strip()
    if re.findall('[^.\d]', kg) or kg == '.' or kg == '':
        print("Wrong value, enter a number".upper())
    else:
        print(kg, "kg is", round(float(kg) * 2.2, 2), "lb", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
