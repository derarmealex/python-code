# 1024|512|256|128|64|32|16|8|4|2|1
while True:
    final = []
    num_to_conv = input("Enter a number to convert in binary: ").strip()
    if num_to_conv.isnumeric():
        num = int(num_to_conv)
        print(f"\n\tDecimal number: {num_to_conv} |==> Binary: {bin(num)}", end="")
        while num > 0:
            ctr = num % 2
            final.append(ctr)
            num //= 2
    else:
        print("\n\tEnter an integer number!\n")
    final = "".join([str(x) for x in final[::-1]])
    print(f"\n\tDecimal number: {num_to_conv} |==> Binary:   {final}\n")
# INPUT
#       Enter a number to convert in binary: 99
# OUTPUT
# 	    Decimal number: 99 |==> Binary: 0b1100011
# 	    Decimal number: 99 |==> Binary:   1100011
