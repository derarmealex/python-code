numbers_to_sum = [1, 2, 3, 4, 5]
index = 3
summus = [0 + number for ix, number in enumerate(numbers_to_sum) if ix < index]
print("Sum of the first", index, "numbers of the list:", numbers_to_sum, "is", sum(summus))
# 6
# or
def summus(numbers_to_sum, index):
    summ = [0 + number for ix, number in enumerate(numbers_to_sum) if ix < index]
    return sum(summ)


print(summus([1, 2, 3, 4, 5], 3))
# 6


# or
def summus(numbers_to_sum, index):
    summ = 0
    ix = 0
    while ix < index:
        summ += numbers_to_sum[ix]
        ix += 1
    return summ


print(summus([1, 2, 3, 4, 5], 3))
# 6
