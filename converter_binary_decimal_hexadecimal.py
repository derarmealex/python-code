# Binary number system: 1024|512|256|128|64|32|16|8|4|2|1
# Hexadecimal number system: 0 1 2 3 4 5 6 7 8 9 A B C D E F
"""
for i in range(0, 16):
    print("%X " % i, end="")
"""

# FROM DECIMAL TO BINARY/HEXADECIMAL
while True:
    final = []
    num_to_convert = input("Enter a number to convert: ").strip()
    while num_to_convert.isnumeric():
        num = int(num_to_convert)
        num_sys = input("Select binary (2) or hexadecimal (16) number system: ").strip()
        if num_sys == "2":
            print(f"\n\tDecimal number: {num_to_convert} |==> Binary: {bin(num)}")
# or
            while num > 0:
                ctr = num % 2
                final.append(ctr)
                num //= 2
            final = "".join([str(x) for x in final[::-1]])
            print(f"\tor\n\tDecimal number: {num_to_convert} |==> Binary:   {final}\n")
            break
        elif num_sys == "16":
            print(f"\n\tDecimal number: {num} |==> Hexadecimal: {hex(num).upper()}")
# or
#            print(f"\tor\n\tDecimal number: {num} |==> Hexadecimal:   {format(num, 'x').upper()}\n")        
            print(f"\tor\n\tDecimal number: {num} |==> Hexadecimal:   {'%x'.upper() % num}\n")
            break
        else:
            print("\n\tCan't convert to this system. Select 2 or 16\n")
    else:
        print("\n\tIncorrect number! Enter an integer\n")
# INPUT
#       Enter a number to convert: 6378
# OUTPUT
# 2:
#       Decimal number: 6378 |==> Binary: 0b1100011101010
#       or
#       Decimal number: 6378 |==> Binary:   1100011101010
# 16:
#       Decimal number: 6378 |==> Hexadecimal: 0X18EA
#       or
#       Decimal number: 6378 |==> Hexadecimal:   18EA
