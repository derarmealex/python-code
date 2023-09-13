for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# or
final = [1]
for number in final:
    if number < 100:
        final.append(number + 1)
for split in final:
    if split % 15 == 0:
        split = "FizzBuzz"
    elif split % 3 == 0:
        split = "Fizz"
    elif split % 5 == 0:
        split = "Buzz"
    print(split)
# or
final = 1
while final < 101:
    print(final)
    final += 1
    if final % 15 == 0:
        print("FizzBuzz")
        final += 1
    elif final % 3 == 0:
        print("Fizz")
        final += 1
    elif final % 5 == 0:
        print("Buzz")
        final += 1
