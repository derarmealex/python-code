from re import findall
while True:
    print("The form of the equation: ax^2+bx+c=0")
    a, b, c = input("Enter coefficient a: ").strip(), input("Enter coefficient b: ").strip(), input("Enter coefficient c: ").strip()
    if findall('[^.\d-]', a) or findall('[^.\d-]', b) or findall('[^.\d-]', c) or a == '.' or b == '.' or c == '.' or a in '' or b in '' or c in '':
        print("\nEnter a correct number!")
    elif a != '0':
        a, b, c = float(a), float(b), float(c)
        d = b ** 2 - 4 * a * c
        if d < 0:
            print('The equation has no solution in the field of real numbers\n')
        elif d == 0:
            x = -b / 2 * a
            print('The equation has one root:\n', x, '\n')
        else:
            x1 = (-b + d ** 0.5) / 2 * a
            x2 = (-b - d ** 0.5) / 2 * a
            print('The equation has two roots:\n', x1, '\n', x2, '\n')
    else:
        print('It is not a quadratic equation!\n')
