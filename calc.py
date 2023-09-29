while True:
    print(
        'Summation:             "+"\n'
        'Subtraction:           "-"\n'
        'Multiplication:        "*"\n'
        'Division:              "/"\n'
        'Exponentiation:        "^"\n'
        '--------------------------'
        )
    oper = input("Choose the operation     : ")
    try:
        num1 = float(input("Enter your first number  : "))
        num2 = float(input("Enter your second number : "))
    except ValueError:
        print("\n\tEnter a correct number!\n")
        continue
    match oper:
        case "+":
            print(f"\t{float(num1)} + {float(num2)} = {float(num1) + float(num2)}\n")
        case "-":
            print(f"\t{float(num1)} - {float(num2)} = {float(num1) - float(num2)}\n")
        case "*":
            print(f"\t{float(num1)} * {float(num2)} = {float(num1) * float(num2)}\n")
        case "/":
            try:
                print(f"\t{float(num1)} / {float(num2)} = {float(num1) / float(num2)}\n")
            except (ZeroDivisionError):
                print("\n\tCouldn't be divided by 0! Enter a correct number\n")
        case "^":
            print(f"\t{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}\n")
        case _:
            print(f"\n\tWrong operator! --> ({oper}) <-- Try again\n")
# or
from re import findall
while True:
    print(
        'Summation:             "+"\n'
        'Subtraction:           "-"\n'
        'Multiplication:        "*"\n'
        'Division:              "/"\n'
        'Exponentiation:        "^"\n'
        '--------------------------'
        )
    oper = input("Choose the operation     : ").strip()
    while oper:
        num1 = input("Enter your first number  : ").strip()
        num2 = input("Enter your second number : ").strip()
        if findall('[^.\d-]', num1) or findall('[^.\d-]', num2) \
                or num1 == '.' or num2 == '.' \
                or num1 == '-' or num2 == '-' \
                or num1 in '' or num2 in '':
            print("\n\tEnter a correct number!\n")
            continue
        elif oper == "+":
            print(f"\t{float(num1)} + {float(num2)} = {float(num1) + float(num2)}\n")
        elif oper == "-":
            print(f"\t{float(num1)} - {float(num2)} = {float(num1) - float(num2)}\n")
        elif oper == "*":
            print(f"\t{float(num1)} * {float(num2)} = {float(num1) * float(num2)}\n")
        elif oper == "/":
            try:
                print(f"\t{float(num1)} / {float(num2)} = {float(num1) / float(num2)}\n")
            except (ZeroDivisionError):
                print("\n\tCouldn't be divided by 0! Enter a correct number\n")
        elif oper == "^":
            print(f"\t{float(num1)} ^ {float(num2)} = {float(num1) ** float(num2)}\n")
        else:
            print(f"\n\tWrong operator! --> ({oper}) <-- Try again\n")
        while True:
            goon = input("\nLike to do another operation?('y' for 'Yes', any other key for 'No'): ").lower().strip()
            if goon == 'y':
                oper = False
                break
            print("\n\tSee ya again!")
            exit()
# INPUT
#       Summation:             "+"
#       Subtraction:           "-"
#       Multiplication:        "*"
#       Division:              "/"
#       Exponentiation:        "^"
#       --------------------------
#       Choose the operation     : ^
#       Enter your first number  : 3
#       Enter your second number : 2
# OUTPUT
#       3.0 ^ 2.0 = 9.0
#       Like to do another operation?('y' for 'Yes', any other key for 'No'): n
#       See ya again!