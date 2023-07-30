sequence = [1, 3, 5, 1, 2, 2, 32, 9, 1, 3, 1]
counts = dict()
for number in sequence:
    if number not in counts:
        counts[number] = 1
    else:
        counts[number] = counts[number] + 1
for key, value in sorted(counts.items()):
    print("Key:", key, "Value:", value)

input()