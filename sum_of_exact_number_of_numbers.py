# II
while True:
    try:
        num_to_sum = int(input("Enter a number to count sum of its digits : "))
# 12345
        index      = int(input("Enter the index how many digits to count  : "))
# 3
    except ValueError:
        print("\n\tEnter a correct number!\n")
    else:
        nums_to_sum = str(num_to_sum)
        nums_to_sum = [num for num in nums_to_sum]
# [1, 2, 3, 4, 5]
        summ = [0 + int(number) for ix, number in enumerate(nums_to_sum) if ix < index]
        print(f"\n\tNumber: {num_to_sum} |==> Sum of its first {index} digits: {sum(summ)}\n")
# INPUT
#       Enter a number to count sum of its digits : 12345
#       Enter the index how many digits to count  : 3
# OUTPUT
#       Number: 12345 |==> Sum of its first 3 digits: 6


# I
def summus(nums_to_sum, index):
    summ = [0 + number for ix, number in enumerate(nums_to_sum) if ix < index]
    return f"\n\tNumber: {num_to_sum} |==> Sum of its first {index} digits: {sum(summ)}\n"


print(summus([1, 2, 3, 4, 5], 3))
# Number: 12345 |==> Sum of its first 3 digits: 6


# III
def summus(nums_to_sum, index):
    summ = 0
    ix = 0
    while ix < index:
        summ += nums_to_sum[ix]
        ix += 1
    return f"\n\tNumber: {num_to_sum} |==> Sum of its first {index} digits: {sum(summ)}\n"


print(summus([1, 2, 3, 4, 5], 3))
# Number: 12345 |==> Sum of its first 3 digits: 6
