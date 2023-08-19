import re
while True:
    gal = input("Enter gallons:\n")
    if re.findall('[^.0123456789]', gal) or gal == '.' or gal == '':
        print("Wrong value, enter a number".upper())
    else:
        print(float(gal), "gal is", round(float(gal)/0.26, 2), "l", "\n")
        while True:
            another_choise = input("Do you have another value to measure? 'y' for 'Yes', any key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Press any key to exit")
                exit()
