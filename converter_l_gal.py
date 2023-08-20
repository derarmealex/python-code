import re
while True:
    l = input("Enter liters:\n")
    if re.findall('[^.\d]', l) or l == '.' or l == '':
        print("Wrong value, enter a number".upper())
    else:
        print(float(l), "l is", round(float(l) * 0.26, 2), "gal", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
