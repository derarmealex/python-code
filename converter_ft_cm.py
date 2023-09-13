import re
while True:
    ft = input("Enter ft:\n").strip()
    if re.findall('[^.\d]', ft) or ft == '.' or ft == '':
        print("Wrong value, enter a number".upper())
    else:
        print(ft, "ft is", round(float(ft) * 30.48, 2), "cm" "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
