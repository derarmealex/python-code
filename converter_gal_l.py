import re
while True:
    gal = input("Enter gallons:\n").strip()
    if re.findall('[^.\d]', gal) or gal == '.' or gal == '':
        print("Wrong value, enter a number".upper())
    else:
        print(gal, "gal is", round(float(gal) / 0.26, 2), "l", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
