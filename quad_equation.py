while True:
    print("The form of equation: ax^2+bx+c=0")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
    except ValueError:
        print("\n\tEnter a correct number!\n")
    else:
        if a != 0:
            d = b ** 2 - 4 * a * c
            if d < 0:
                print("\n\tThe equation has no solution in the field of real numbers.\n")
            elif d == 0:
                x = -b / 2 * a
                if x == -0: print("\n\tThe equation has one root: ", abs(x), "\n")
                else: print("\n\tThe equation has one root: ", x, "\n")
            else:
                x1 = round((-b + d ** 0.5) / 2 * a, 2)
                x2 = round((-b - d ** 0.5) / 2 * a, 2)
                print(f"\n\tThe equation has two roots:\n\t{x1}\n\t{x2}\n")
        else:
            print('\n\tIt is not a quadratic equation!\n')
# or
from re import findall
while True:
    print("The form of equation: ax^2+bx+c=0")
    a = input("Enter coefficient a: ").strip()
    b = input("Enter coefficient b: ").strip()
    c = input("Enter coefficient c: ").strip()
    if findall('[^.\d-]', a) or findall('[^.\d-]', b) or findall('[^.\d-]', c) \
            or a == '.' or b == '.' or c == '.' \
            or a in '' or b in '' or c in '':
        print("\n\tEnter a correct number!\n")
    elif a != '0':
        a, b, c = float(a), float(b), float(c)
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("\n\tThe equation has no solution in the field of real numbers.\n")
        elif d == 0:
            x = -b / 2 * a
            if x == -0: print("\n\tThe equation has one root: ", abs(x), "\n")
            else: print("\n\tThe equation has one root: ", x, "\n")
        else:
            x1 = round((-b + d ** 0.5) / 2 * a, 2)
            x2 = round((-b - d ** 0.5) / 2 * a, 2)
            print(f"\n\tThe equation has two roots:\n\t{x1}\n\t{x2}\n")
    else:
        print('\n\tIt is not a quadratic equation!\n')
