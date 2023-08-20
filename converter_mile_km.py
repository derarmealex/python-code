import re
while True:
    mile = input("Enter miles:\n")
    if re.findall('[^.\d]', mile) or mile == '.' or mile == '':
        print("Wrong value, enter a number".upper())
    else:
        print(float(mile), "mile is", round(float(mile) / 0.62, 2), "km", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
