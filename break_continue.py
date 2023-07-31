mlt_three = []
number = (1, 2, 3, 4, 5)
for number in number:                       # !a wrong variable
    if number % 3 == 0: 
        mlt_three.append(number)
        break
    print(number)
print("found multiple of three:", mlt_three)
print(number)                               # because of the wrong variable

for sentence in "be near":
    if sentence in {"e", "r"}:
        continue
    print("Value", sentence, "is important")
print(sentence)
