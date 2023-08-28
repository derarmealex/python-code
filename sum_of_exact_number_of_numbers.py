def fungus(x, n):
    a = 0
    w = 0
    while w < n:
        a += x[w]
        w += 1
    return a
print(fungus([1, 2, 3, 4, 5], 3))
# or
def fungus(x, n):
    q = 0
    for ix, number in enumerate(x):
        if ix < n:
            q += number
    return q
print(fungus([1, 2, 3, 4, 5], 3))
# or
def fungus(x, n):
    q = [0 + number for ix, number in enumerate(x) if ix < n]
    return sum(q)
print(fungus([1, 2, 3, 4, 5], 3))