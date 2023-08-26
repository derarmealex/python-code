def fungus(x, y):
    if y % x == 0:
        return x
    for z in range(y, 0, -1):
        if y % z == 0 and x % z == 0:
            return z
print(fungus(19, 21))
print(fungus(36, 12))
print(fungus(12, 17))
print(fungus(6, 4))
print(fungus(360, 336))