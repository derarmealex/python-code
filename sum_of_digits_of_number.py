while True:
    x = input('Enter a number to calculate sum of digits: ')
    if x.isnumeric():
        final = sum([0 + int(x) for x in str(x)])
        print('Sum of digits of the number is', final)
    else:
        print("Wrong value, enter a number".upper())