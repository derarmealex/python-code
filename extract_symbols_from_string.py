sentence = input('Enter a phrase to analyse: ').lower().strip()                     # 'What about Route66?..'
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
