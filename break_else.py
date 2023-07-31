for letter in ("a", "b", "c", "d"):
    print(letter.upper())
else:
    print("All the letters are written down")
    
print("\n")

for letter in ("a", "b", "c", "d"):
    if letter == "4":
        print("Found '4', skip the cycle")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("All the letters are written down")

print("Go on the loop")

print("\n")

for letter in ("a", "b", "c", "d"):
    if letter == "c":
        print("Found 'c', skip the cycle")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("All the letters are written down")
    
print("Go on the loop")
