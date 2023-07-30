for stg in "abcd":
    print(stg + "3")

for stg2 in "go on", "waw":
    print(stg2)
    
for lst in [1, 2, 3, 4, 5]:
    print(lst ** 2)

for lst2 in ["a", "b", "c", "d"]:
    print(lst2 * 2)

for dct in {"Name": "Alex", "Surname": "Green", "Password": "123"}:
    print(dct)
    
lst2 = iter(["a", "b", "c"])
print(next(lst2)*2)
print(next(lst2))
print(next(lst2) + "e")
#StopIteration print(next(lst2)) 

for st in {"*", "%", "waha", "wwah", "wah"}:   # like list/tuple, but arranged hierarchically (randomly?)
    print(st)
    
lst3 = (1, 2, 3)
for number in lst3:
    print(number)

input()