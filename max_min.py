def max_min(data):
    mx = data[0]
    mn = data[0]
    for num in data:
        if num > mx:
            mx = num
        elif num < mn:
            mn = num
    return mx, mn               # (75, -5)


print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
