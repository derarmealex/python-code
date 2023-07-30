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

input()

for number in range(1, 101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
input()