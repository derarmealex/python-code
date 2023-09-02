import re
while True:
    cm = input("Enter cm:\n")
    if re.findall('[^.\d]', cm) or cm == '.' or cm == '':
        print("Wrong value, enter a number".upper())
    else:
        q = round(float(cm) / 30.48, 2)
        w = str(q).split('.')[-1]
        if w == '0':
            print(cm, "cm is", int(q), "ft", "\n")
        else:
            print(cm, "cm is", int(q), "ft", round(int(w) / 12, 2), "inch" "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()