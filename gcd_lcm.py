def gcd_lcm(x, y):
    gcd = 1
    if y > x and y % x == 0:
        return (f'{x} | {y * x / x}')
    elif y < x and x % y == 0:
        return (f'{y} | {y * x / y}')
    for z in range(y, 0, -1):
        if y % z == 0 and x % z == 0:
            gcd = z
            break
    return (f'{gcd} | {y * x / gcd}')
print('gcd | lcm of 3, 15 is', gcd_lcm(3, 15))          # gcd | lcm of 3, 15 is 3 | 15.0
print('gcd | lcm of 19, 21 is', gcd_lcm(19, 21))        # gcd | lcm of 19, 21 is 1 | 399.0
print('gcd | lcm of 36, 12 is', gcd_lcm(36, 12))        # gcd | lcm of 36, 12 is 12 | 36.0
print('gcd | lcm of 15, 17 is', gcd_lcm(15, 17))        # gcd | lcm of 15, 17 is 1 | 255.0
print('gcd | lcm of 6, 4 is', gcd_lcm(6, 4))            # gcd | lcm of 6, 4 is 2 | 12.0
print('gcd | lcm of 360, 336 is', gcd_lcm(360, 336))    # gcd | lcm of 360, 336 is 24 | 5040.0