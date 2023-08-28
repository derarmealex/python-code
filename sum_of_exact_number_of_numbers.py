def summus(x, n):
    summ = 0
    ix = 0
    while ix < n:
        summ += x[ix]
        ix += 1
    return summ
print(summus([1, 2, 3, 4, 5], 3))
# or
def summus(x, n):
    summ = [0 + number for ix, number in enumerate(x) if ix < n]
    return sum(summ)
print(summus([1, 2, 3, 4, 5], 3))
