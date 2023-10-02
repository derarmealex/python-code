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


# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = ?
collection = []
# [9.0, '^', 2.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
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
fin_col = " ".join([str(x) for x in collection])
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0
#print(fin_col)
col = collection
# [9.0, '^', 2.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
#print(col)
#print(list(enumerate(col)))
# 1: [(0, 9.0), (1, '^'), (2, 2.0), (3, '+'), (4, 1), (5, '-'), (6, 3.5), (7, '*'), (8, 0.0),
# (9, '/'), (10, 2.0), (11, '^'), (12, 5.0), (13, '*'), (14, 7.0), (15, '*'), (16, 10.0)]
# 2: [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 3.5), (5, '*'), (6, 0.0), (7, '/'),
# (8, 2.0), (9, '^'), (10, 5.0), (11, '*'), (12, 7.0), (13, '*'), (14, 10.0)]
index_move = 0
if "^" in col:
    for ix, item in enumerate(col):
        if item == "^":                         # 1: (1, '^')   2: (9, '^')
#            print(list(enumerate(col)))
            ix -= index_move
#            print(ix)                           # 1: 1          2: 9
            num1 = col[ix - 1]                  # 1: 9.0        2: 2.0
#            print(num1)
            num2 = col[ix + 1]                  # 1: 2.0        2: 5.0
#            print(num2)
# 1: [9.0, '^', 2.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
#            print(col)
            pow_res = expon(num1, num2)         # 1: 81.0       2: 32.0
#            print(pow_res)
            col[ix - 1] = pow_res
# 1: [81.0, '^', 2.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 32.0, '^', 5.0, '*', 7.0, '*', 10.0]
#            print(col)
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
# 1: [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 2.0, '^', 5.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 32.0, '*', 7.0, '*', 10.0]
#            print(col)
            index_move += 2
#print(list(enumerate(col)))
# [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 3.5), (5, '*'), (6, 0.0),
# (7, '/'), (8, 32.0), (9, '*'), (10, 7.0), (11, '*'), (12, 10.0)]
index_move = 0
if "/" in col:
    for ix, item in enumerate(col):
        if item == "/":                         # (7, '/')
#            print(list(enumerate(col)))
            ix -= index_move
#            print(ix)                           # 7
            num1 = col[ix - 1]                  # 0.0
#            print(num1)
            num2 = col[ix + 1]                  # 32.0
#            print(num2)
# [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 32.0, '*', 7.0, '*', 10.0]
#            print(col)
            try:
                div_res = divis(num1, num2)     # 0.0
            except ZeroDivisionError:
                print("\n\tCouldn't be divided by 0! Expression has no solution\n")
                exit()
#            print(div_res)
            col[ix - 1] = div_res
# [81.0, '+', 1, '-', 3.5, '*', 0.0, '/', 32.0, '*', 7.0, '*', 10.0]
#            print(col)
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
# [81.0, '+', 1, '-', 3.5, '*', 0.0, '*', 7.0, '*', 10.0]
#            print(col)
            index_move += 2
#print(list(enumerate(col)))
# 1: [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 3.5), (5, '*'),
# (6, 0.0), (7, '*'), (8, 7.0), (9, '*'), (10, 10.0)]
# 2: [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 0.0), (5, '*'),
# (6, 7.0), (7, '*'), (8, 10.0)]
# 3: [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 0.0), (5, '*'), (6, 10.0)]
index_move = 0
if "*" in col:
    for ix, item in enumerate(col):
        if item == "*":                         # 1: (5, '*')  2: (5, '*')  3: (5, '*')
#            print(list(enumerate(col)))
            ix -= index_move
#            print(ix)                           # 1: 5         2: 5         3: 5
            num1 = col[ix - 1]                  # 1: 3.5       2: 0.0       3: 0.0
#            print(num1)
            num2 = col[ix + 1]                  # 1: 0.0       2: 7.0       3: 10.0
#            print(num2)
# 1: [81.0, '+', 1, '-', 3.5, '*', 0.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 0.0, '*', 7.0, '*', 10.0]
# 3: [81.0, '+', 1, '-', 0.0, '*', 10.0]
#            print(col)
            mult_res = mult(num1, num2)         # 1: 0.0       2: 0.0       3: 0.0
#            print(mult_res)
            col[ix - 1] = mult_res
# 1: [81.0, '+', 1, '-', 0.0, '*', 0.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 0.0, '*', 7.0, '*', 10.0]
# 3: [81.0, '+', 1, '-', 0.0, '*', 10.0]
#            print(col)
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
# 1: [81.0, '+', 1, '-', 0.0, '*', 7.0, '*', 10.0]
# 2: [81.0, '+', 1, '-', 0.0, '*', 10.0]
# 3: [81.0, '+', 1, '-', 0.0]
#            print(col)
            index_move += 2
#print(list(enumerate(col)))
# [(0, 81.0), (1, '+'), (2, 1), (3, '-'), (4, 0.0)]
index_move = 0
if "-" in col:
    for ix, item in enumerate(col):
        if item == "-":                         # (3, '-')
#            print(list(enumerate(col)))
            ix -= index_move
#            print(ix)                           # 3
            num1 = col[ix - 1]                  # 1
#            print(num1)
            num2 = col[ix + 1]                  # 0.0
#            print(num2)
# [81.0, '+', 1, '-', 0.0]
#            print(col)
            sub_res = minus(num1, num2)         # 0.0
#            print(sub_res)
            col[ix - 1] = sub_res
# [81.0, '+', 1.0, '-', 0.0]
#            print(col)
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
# [81.0, '+', 1.0]
#            print(col)
            index_move += 2
#print(list(enumerate(col)))
# [(0, 81.0), (1, '+'), (2, 1.0)]
index_move = 0
if "+" in col:
    for ix, item in enumerate(col):
        if item == "+":                         # (1, '+')
#            print(list(enumerate(col)))
            ix -= index_move
#            print(ix)                           # 1
            num1 = col[ix - 1]                  # 81.0
#            print(num1)
            num2 = col[ix + 1]                  # 1.0
#            print(num2)
# [81.0, '+', 1.0]
#            print(col)
            sum_res = plus(num1, num2)          # 82.0
#            print(sum_res)
            col[ix - 1] = sum_res
# [82.0, '+', 1.0]
#            print(col)
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
# [82.0]
#            print(col)
            index_move += 2
#print(list(enumerate(col)))
# [(0, 82.0)]
result = col[0]                                 # [82.0]
print(f"\n\t{fin_col} = {result}\n")
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = 82.0
