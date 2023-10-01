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


# 1.0 + 2.0 ** 2 --3.0 * 0.1 / 99.0 ** 2.5
collection = [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
col = collection
copy_col = col.copy()
# [(0, 1.0), (1, '+'), (2, 2.0), (3, '^'), (4, 2.0), (5, '-'), (6, -3.0), (7, '*'), (8, 0.1), (9, '/'), (10, 99.0), (11, '^'), (12, 2.5)]
if "^" in col:
    step = 0
    for ix, item in enumerate(col):
        if item == "^":                 # (3, '^')  #(11, '^')
#            print(ix)
            p = col[ix - 1]             # 2.0       # 99.0
#            print(p)
            ow = col[ix + 1]            # 2.0       # 2.5
#            print(ow)
# [1.0, '+', 2.0, '^', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
#            print(copy_col)
            temp_slice = copy_col[:ix-step]
            temp_slice2 = copy_col[ix+2-step:]
            copy_col = temp_slice + temp_slice2
# [1.0, '+', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0]
#            print(copy_col)
            pow_res = expon(p, ow)      # 4.0       # 97518.71871081983
#            print(pow_res)
            copy_col[ix - 1-step] = pow_res
# [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
# [1.0, '+', 4.0, '-', -3.0, '*', 0.1, '/', 97518.71871081983]
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
