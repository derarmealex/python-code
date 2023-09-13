from re import findall
while True:
    print(
        'Summation:        "+"\n'
        'Subtraction:      "-"\n'
        'Multiplication:   "*"\n'
        'Division:         "/"\n'
        'Exponentiation:   "^"\n'
        '---------------------')
    oper = input("Choose the operation: ").strip()
    if oper not in ('+', '-', '*', '/', '^'):
        print("Wrong operator! Try again.")
        continue
    else:
        ctr = True
        while ctr:
            num1, num2 = input("Enter your first number: ").strip(), input("Enter your second number: ").strip()
            if findall('[^.\d]', num1) or findall('[^.\d]', num2) or num1 == '.' or num2 == '.':
                print("Enter a number!")
                continue
            elif oper == "+":
                print(f"{float(num1)} + {float(num2)} = {float(num1) + float(num2)}")
            elif oper == "-":
                print(f"{float(num1)} - {float(num2)} = {float(num1) - float(num2)}")
            elif oper == "*":
                print(f"{float(num1)} * {float(num2)} = {float(num1) * float(num2)}")
            elif oper == "/":
                print(f"{float(num1)} / {float(num2)} = {float(num1) / float(num2)}")
            else:
                print(f"{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}")
            while True:
                goon = input("Like to do another operation?('y' for 'Yes', any other key for 'No'): ").lower()
                if goon == 'y':
                    ctr = False
                    break
                else:
                    exit()
