def plus(*x):
#    return f"\tSum of numbers -->{x}--> is ==>({sum(x)})<==\n"
    return sum(x)


def minus(*x):
    x = [-x for x in x]
# [-1, -2, 3, -4, 5]
    x[0] = -x[0]
# [1, -2, 3, -4, 5]
#    return f"\tDifference of numbers -->{x}--> is ==>({sum(x)})<==\n"
    return sum(x)


def mult(*x):
    num = x[0]
    i = 0
    while i < len(x) - 1:
        num = num * x[i + 1]
        i += 1
#    return f"\tProduct of numbers -->{x}--> is ==>({num})<==\n"
    return num


def divis(*x):
    num = x[0]
    i = 0
    while i < len(x) - 1:
        num = num / x[i + 1]
        i += 1
#    return f"\tQuotient of numbers -->{x}--> is ==>({num})<==\n"
    return num


def expon(x, n):
    num = pow(x, n)
#    return f"\t{n} ** {x} = {num}\n"
    return num


#print(plus(1, 2, -3, 4, -5))
# Sum of numbers -->(1, 2, -3, 4, -5)--> is ==>(-1)<==
#print(minus(1, 2, -3, 4, -5))
# Difference of numbers -->[1, -2, 3, -4, 5]--> is ==>(3)<==
#print(mult(1, 2, -3, 4, -5))
# Product of numbers -->(1, 2, -3, 4, -5)--> is ==>(120)<==
#print(divis(1, 2, -3, 4, -5))
# Quotient of numbers -->(1, 2, -3, 4, -5)--> is ==>(120)<==
#print(expon(2, -3))
# -3 ** 2 = 0.125


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
            print(f"\n\t{float(num1)} + {float(num2)} = {plus(num1, num2)}\n")
            num1 = float(num1) + float(num2)
        case "-":
            print(f"\n\t{float(num1)} - {float(num2)} = {minus(num1, num2)}\n")
            num1 = float(num1) - float(num2)
        case "*":
            print(f"\n\t{float(num1)} * {float(num2)} = {mult(num1, num2)}\n")
            num1 = float(num1) * float(num2)
        case "/":
            try:
                print(f"\n\t{float(num1)} / {float(num2)} = {divis(num1, num2)}\n")
            except ZeroDivisionError:
                print("\n\tCouldn't be divided by 0! Enter a correct number\n")
            num1 = float(num1) / float(num2)
        case "^":
            print(f"\n\t{float(num1)} ^ {float(num2)} = {expon(num1, num2)}\n")
            num1 = float(num1) ** float(num2)
        case _:
            print(f"\n\tWrong operator selected! --> ({oper}) <-- Try again\n")
