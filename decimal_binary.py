while True:
    final = []
    x = input('Enter a number: ')
    if x.isnumeric():
        x = int(x)
        print(bin(x))
        while x > 0:
            y = x % 2
            final.append(y)
            y = x // 2
            x = y
    else:
        print('Enter an integer number!'.upper())
    z = ''.join([str(x) for x in final[::-1]])
    print(f'{z:>08s}')