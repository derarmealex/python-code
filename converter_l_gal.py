from re import findall
while True:
    lt = input("Enter liters: ").strip()
    if findall('[^0-9.]', lt) or lt == '0' or lt == '.' or lt in '':
        print("Enter a correct number!")
    else:
        print(lt, "lt is", round(float(lt) * 0.26, 2), "gal", "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                exit()
