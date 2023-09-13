from re import findall
while True:
    lt = input("Enter liters:\n").strip()
    if findall('[^.\d]', lt) or lt == '.' or lt == '':
        print("Wrong value, enter a number!".upper())
    else:
        print(lt, "lt is", round(float(lt) * 0.26, 2), "gal", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                input("Any key to exit")
                exit()
