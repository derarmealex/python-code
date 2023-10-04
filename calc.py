# I
num1 = ""
while not num1:
    try:
        num1 = float(input("Enter your first number : "))
    except ValueError:
        print("\n\tIncorrect number! Try again\n")
while True:
    print(
        'Summation:            "+"\n'
        'Subtraction:          "-"\n'
        'Multiplication:       "*"\n'
        'Division:             "/"\n'
        'Exponentiation:       "^"\n'
        '-------------------------\n'
        '\tYour expression to process now:', num1
        )
    oper = input("Choose the operation    : ")
    try:
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("\n\tIncorrect number! Try again\n")
        continue
    match oper:
        case "+":
            print(f"\n\t{float(num1)} + {float(num2)} = {float(num1) + float(num2)}\n")
            num1 = float(num1) + float(num2)
        case "-":
            print(f"\n\t{float(num1)} - {float(num2)} = {float(num1) - float(num2)}\n")
            num1 = float(num1) - float(num2)
        case "*":
            print(f"\n\t{float(num1)} * {float(num2)} = {float(num1) * float(num2)}\n")
            num1 = float(num1) * float(num2)
        case "/":
            try:
                print(f"\n\t{float(num1)} / {float(num2)} = {float(num1) / float(num2)}\n")
            except ZeroDivisionError:
                print("\n\tCouldn't be divided by 0! Enter a correct number\n")
            num1 = float(num1) / float(num2)
        case "^":
            print(f"\n\t{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}\n")
            num1 = float(num1) ** float(num2)
        case _:
            print(f"\n\tWrong operator selected! --> ({oper}) <-- Try again\n")
# II
from re import findall
num1 = ""
while not num1:
    num1 = input("Enter your first number : ")
    if findall('[^0-9.-]', num1) or num1 == '.' or num1 == '-' or num1 in '' :
        print("\n\tIncorrect number! Try again\n")
        num1 = ""
while True:
    print(
        'Summation:            "+"\n'
        'Subtraction:          "-"\n'
        'Multiplication:       "*"\n'
        'Division:             "/"\n'
        'Exponentiation:       "^"\n'
        '-------------------------\n'
        '\tYour expression to process now:', num1
        )
    oper = input("Choose the operation    : ")
    num2 = input("Enter your second number: ").strip()
    if findall('[^0-9.-]', num2) or num2 == '.' or num2 == '-' or num2 in '':
        print("\n\tIncorrect number! Try again\n")
    elif oper == "+":
        print(f"\n\t{float(num1)} + {float(num2)} = {float(num1) + float(num2)}\n")
        num1 = float(num1) + float(num2)
    elif oper == "-":
        print(f"\n\t{float(num1)} - {float(num2)} = {float(num1) - float(num2)}\n")
        num1 = float(num1) - float(num2)
    elif oper == "*":
        print(f"\n\t{float(num1)} * {float(num2)} = {float(num1) * float(num2)}\n")
        num1 = float(num1) * float(num2)
    elif oper == "/":
        try:
            print(f"\n\t{float(num1)} / {float(num2)} = {float(num1) / float(num2)}\n")
        except ZeroDivisionError:
            print("\n\tCouldn't be divided by 0! Enter a correct number\n")
        num1 = float(num1) / float(num2)
    elif oper == "^":
        print(f"\n\t{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}\n")
        num1 = float(num1) ** float(num2)
    else:
        print(f"\n\tWrong operator selected! --> ({oper}) <-- Try again\n")
