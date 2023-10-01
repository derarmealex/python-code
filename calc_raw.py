collection = []
# [1.0, '+', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]
while True:
    try:
        num = float(input("Enter [next] number to calculate: "))
        print("")
    except ValueError:
        print(f"\n\tIncorrect item! Try again")
        print("\tYour collection to process:", collection)
        continue
    else:
        collection.append(float(num))
#        print("\n\tYour collection to process:", collection, "\n")
        oper_ctr = True
        while oper_ctr:
            print("\tYour collection to process:", collection, "")
            oper = input(
                        'Summation     : "+"\n'
                        'Subtraction   : "-"\n'
                        'Multiplication: "*"\n'
                        'Division      : "/"\n'
                        'Exponentiation: "^"\n'
                        '-------------------\n'
                        "Enter operator, or print 'start' to stop input and start calculating: "
                        ).strip()
            print("")
            if oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^":
                collection.append(oper)
                print("\tYour collection to process now:", collection, "\n")
                oper_ctr = False
#            elif oper != "+" and oper != "-" and oper != "*" and oper != "/" and oper != "^":
            else:
                print(f"\tWrong operator! --> ({oper}) <-- Try again")
                oper_ctr = True
# Your collection to process: [1.0, '+', 2.0, '-', -3.0, '*', 0.1, '/', 99.0, '^', 2.5]


#plus(ent)


"""
def plus(*x):
    return f"\tSum of numbers -->{x}--> is ==>({sum(x)})<==\n"
# Sum of numbers -->(1, 2, -3, 4, -5)--> is ==>(-1)<==


def minus(*x):
    x = [-x for x in x]
# [-1, -2, 3, -4, 5]
    x[0] = -x[0]
# [1, -2, 3, -4, 5]
    return f"\tDifference of numbers -->{x}--> is ==>({sum(x)})<==\n"
# Difference of numbers -->[1, -2, 3, -4, 5]--> is ==>(3)<==


def mult(*x):
    num = x[0]
    i = 0
    while i < len(x) - 1:
        num = num * x[i + 1]
        i += 1
    return f"\tProduct of numbers -->{x}--> is ==>({num})<==\n"
# Product of numbers -->(1, 2, -3, 4, -5)--> is ==>(120)<==


def divis(*x):
    num = x[0]
    i = 0
    while i < len(x) - 1:
        num = num / x[i + 1]
        i += 1
    return f"\tQuotient of numbers -->{x}--> is ==>({num})<==\n"
# Quotient of numbers -->(1, 2, -3, 4, -5)--> is ==>(120)<==


def expon(x, n):
    num = pow(x, n)
    return f"\t{n} ** {x} = {num}\n"
# -3 ** 2 = 0.125


print(plus(1, 2, -3, 4, -5))
print(minus(1, 2, -3, 4, -5))
print(mult(1, 2, -3, 4, -5))
print(divis(1, 2, -3, 4, -5))
print(expon(2, -3))
"""