collection = []
# [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
main_ctr = True
while main_ctr:
    try:
        num = float(input("Enter [next] number to calculate: "))
        print("")
    except ValueError:
        print(f"\n\tIncorrect number! Try again")
        print("\tYour collection to process:", collection)
        continue
    else:
        collection.append(num)
#        print("\n\tYour collection to process:", collection, "\n")
        while True:
            print("\tYour collection to process:", collection, "")
            oper = input(
                        'Summation     : "+"\n'
                        'Subtraction   : "-"\n'
                        'Multiplication: "*"\n'
                        'Division      : "/"\n'
                        'Exponentiation: "^"\n'
                        '-------------------\n'
                        "Enter operator, or print 'start' to break input and start calculating: "
                        ).strip().lower()
            print("")
            if oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^":
                collection.append(oper)
                print("\tYour collection to process now:", collection, "\n")
                break
            elif oper == "start":
                main_ctr = False
                break
            else:
                print(f"\tWrong operator! --> ({oper}) <-- Try again")
#print("\tYour collection to process:", collection)
# Your collection to process: [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
fin_col = " ".join([str(x) for x in collection])
print(fin_col)
# 1.0 + 2.0 ^ 2.0 - -3.0 * 0.1 / 99.0 ^ 2.5
collection = [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
col = collection
copy_col = col.copy()
# [(0, 1.0), (1, '+'), (2, 2.0), (3, '^'), (4, 2.0), (5, '-'), (6, -3.0), (7, '*'), (8, 0.1), (9, '/'), (10, 99.0), (11, '^'), (12, 2.5)]
if "^" in col:
    step = 0
    for ix, item in enumerate(col):
        if item == "^":                 # (3, '^')  #(11, '^')
#            print(ix)                  # 3         # 11
            p = col[ix - 1]             # 2.0       # 99.0
#            print(p)
            ow = col[ix + 1]            # 2.0       # 2.5
#            print(ow)
# 1: [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# 2: [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
#            print(copy_col)
            temp_slice = copy_col[:ix-step]
            temp_slice2 = copy_col[ix+2-step:]
            copy_col = temp_slice + temp_slice2
# 1: [1.0, '+', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# 2: [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0]
#            print(copy_col)
            pow_res = p ** ow           # 4.0       # 97518.71871081983
#            print(pow_res)
            copy_col[ix - 1-step] = pow_res
# 1: [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# 2: [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 97518.71871081983]
#            print(copy_col)
            step += 2
print(copy_col)

if "/" in col:
    for ix, item in enumerate(col):
        if item == "^":
            p = col[ix - 1]             # 2.0   # 99.0
#if *


print(col)
# [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]

# ANCIENT
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
