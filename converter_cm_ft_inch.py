from re import findall
while True:
    cm = input("Enter cm: ").strip()
    if findall('[^.\d]', cm) or cm == '0' or cm == '.' or cm in '':
        print("Enter a correct number!")
    else:
        rough = round(float(cm) / 30.48, 2)
        fract = str(rough).split('.')[-1]
        if fract == '0':
            print(cm, "cm is", int(rough), "ft\n")
        else:
            print(cm, "cm is", int(rough), "ft", round(int(fract) / 12, 2), "inch\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
