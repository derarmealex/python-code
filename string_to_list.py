stg = "1, 2, 3, 4, 5"
#final = []

stg2 = stg.split(",")
print(stg2)

#for item in stg2:
#    clear = int(item.strip())
#    final.append(clear)

final = [int(item.strip()) for item in stg2]

print("List:", final)

input()