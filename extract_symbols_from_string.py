sentence = input('Enter a phrase to analyse: ')                             # 'What about Route66?..'
con = "bcdfghjklmnpqrstvwxz"
vow = "aeiouy"
num = "1234567890"
final = {"Consonants": 0, "Vowels": 0, "Numbers": 0, "Other symbols": 0}
for i in sentence:
    if i in con:
        final["Consonants"] += 1
    elif i in vow:
        final["Vowels"] += 1
    elif i in num:
        final["Numbers"] += 1
    else:
        final["Other symbols"] += 1
print(
    "Consonants:", final["Consonants"], "|", "Vowels:", final["Vowels"], "|",
    "Numbers:", final["Numbers"], "|", "Other symbols:", final["Other symbols"]
    )
# Consonants: 5 | Vowels: 7 | Numbers: 2 | Other symbols: 7
print(" | ".join([f"{key}: {value}" for key, value in final.items()]))
# Consonants: 5 | Vowels: 7 | Numbers: 2 | Other symbols: 7


# BOOL
def fc(z):
    print([f"{z} - {z in x}" for z in z if z in x])                         # ['u - True', 'e - True', 'i - ...
    print([f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z])  # ['Z - False', 'v - False', 'u -  ...


fc(z)
# GENERATOR
gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(gen))                                                            # Z - False
print(next(gen))                                                            # v - False
print(next(gen))                                                            # u - True
print(next(gen))                                                            # k - False


# or
def fungus():
    for z in z:
        yield z


gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
print(next(gen))                                                            # Z - False
print(next(gen))                                                            # v - False
print(next(gen))                                                            # u - True


# or
def fungus():
    for z in z:
        yield z


gen = (f"{z} - {z in x}" if z in x else f"{z} - {z in x}" for z in z)
itr = 0
while itr < len(z):                                                         # Z - False
    print(next(gen))                                                        # v - False
    itr += 1                                                                # u - True ...
