import re
while True:
    km = input("Enter kilometres:\n")
    if re.findall('[^.\d]', km) or km == '.' or km == '':
        print("Wrong value, enter a number".upper())
    else:
        print(float(km), "km is", round(float(km) * 0.62, 2), "mile", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
