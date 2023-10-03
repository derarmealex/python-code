sentence = input('Enter a phrase to analyse: ').lower().strip()     # 'What about Route66?..'
cons = "bcdfghjklmnpqrstvwxz"
vows = "aeiouy"
num = "1234567890"
final = {"Consonants": 0, "Vowels": 0, "Numbers": 0, "Others": 0}
for i in sentence:
    if i in cons:
        final["Consonants"] += 1
    elif i in vows:
        final["Vowels"] += 1
    elif i in num:
        final["Numbers"] += 1
    else:
        final["Others"] += 1
print(
    "Consonants:", final["Consonants"], "|", "Vowels:", final["Vowels"], "|",
    "Numbers:", final["Numbers"], "|", "Others:", final["Others"]
    )
# Consonants: 5 | Vowels: 7 | Numbers: 2 | Others: 7
# or
print(" | ".join([f"{key}: {value}" for key, value in final.items()]))
# Consonants: 5 | Vowels: 7 | Numbers: 2 | Others: 7
