numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = 0
odd = 0

for number in numbers:
	if number %2 == 0:
		even = even + number
	else:
		odd = odd + number
final = abs(even - odd)

print("Difference is:", final)

input()