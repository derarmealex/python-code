sentence = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
vowels = "eyuioa"
final = {"Vowels": 0, "Consonants": 0}
for letter in sentence:
    if not letter.isalpha():
        continue
    elif letter in vowels:
        final["Vowels"] = final["Vowels"] + 1
    else:
        final["Consonants"] = final["Consonants"] + 1

print("Consonants:", final["Consonants"], "|", "Vowels:", final["Vowels"])

input()
