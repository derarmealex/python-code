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
