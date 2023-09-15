from re import findall
while True:
    print(
        'Summation:        "+"\n'
        'Subtraction:      "-"\n'
        'Multiplication:   "*"\n'
        'Division:         "/"\n'
        'Exponentiation:   "^"\n'
        '---------------------'
        )
    oper = input("Choose the operation: ").strip()
    if oper not in ('+', '-', '*', '/', '^'):
        print("Wrong operator! Try again\n")
        continue
    else:
        ctr = True
        while ctr:
            num1 = input("Enter your first number: ").strip()
            num2 = input("Enter your second number: ").strip()
            if findall('[^.\d-]', num1) or findall('[^.\d-]', num2) \
                    or num1 == '.' or num2 == '.' \
                    or num1 in '' or num2 in '':
                print("\nEnter a correct number!")
                continue
            elif oper == "+":
                print(f"{float(num1)} + {float(num2)} = {float(num1) + float(num2)}")
            elif oper == "-":
                print(f"{float(num1)} - {float(num2)} = {float(num1) - float(num2)}")
            elif oper == "*":
                print(f"{float(num1)} * {float(num2)} = {float(num1) * float(num2)}")
            elif oper == "/":
                try:
                    print(f"{float(num1)} / {float(num2)} = {float(num1) / float(num2)}")
                except (ZeroDivisionError):
                    print("couldn't be divised by 0!\n")
            else:
                print(f"{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}")
            while True:
                goon = input("Like to do another operation?('y' for 'Yes', any other key for 'No'): ").lower().strip()
                if goon == 'y':
                    ctr = False
                    break
                else:
                    exit()
