while True:
    final = []
    x = input('Enter a number: ').strip()           # 99
    if x.isnumeric():
        x = int(x)
        print(bin(x))                               # 0b1100011
        while x > 0:
            y = x % 2
            final.append(y)
            x //= 2
    else:
        print('\nEnter an integer number!')
    final = ''.join([str(x) for x in final[::-1]])
    print(f'{final:>08s}')                          # 01100011
