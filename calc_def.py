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


# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = 82.0
collection = []
main_ctr = True
while main_ctr:
    try:
        num = float(input("Enter [next] number to calculate: "))
        print("")
    except ValueError:
        print(f"\n\tIncorrect number! Try again")
        print("\tYour collection to process now:", collection)
        continue
    else:
        collection.append(num)
        while True:
            print("\tYour collection to process:", collection, "")
            oper = input(
                        'Summation     : "+"\n'
                        'Subtraction   : "-"\n'
                        'Multiplication: "*"\n'
                        'Division      : "/"\n'
                        'Exponentiation: "^"\n'
                        '-------------------\n'
                        "Select operator, or print 'start' to break input and start calculating: "
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
fin_col = " ".join([str(x) for x in collection])
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = ?
print(fin_col + " = ?")
col = collection
index_move = 0
if "^" in col:
    for ix, item in enumerate(col):
        if item == "^":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            pow_res = expon(num1, num2)
            col[ix - 1] = pow_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "/" in col:
    for ix, item in enumerate(col):
        if item == "/":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            try:
                div_res = divis(num1, num2)
            except ZeroDivisionError:
                print(f"\n\t{num1} / {num2} --> couldn't be divided by 0! Expression has no solution\n")
                exit()
            col[ix - 1] = div_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "*" in col:
    for ix, item in enumerate(col):
        if item == "*":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            mult_res = mult(num1, num2)
            col[ix - 1] = mult_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "-" in col:
    for ix, item in enumerate(col):
        if item == "-":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            sub_res = minus(num1, num2)
            col[ix - 1] = sub_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "+" in col:
    for ix, item in enumerate(col):
        if item == "+":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            sum_res = plus(num1, num2)
            col[ix - 1] = sum_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
result = col[0]
print(f"\n\t{fin_col} = {result}\n")
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = 82.0
