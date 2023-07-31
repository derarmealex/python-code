user = dict(Name= "Marek", Password= "1234")

print("Enter your username:")
n = input()
print("Enter your password:")
p = input()

if bool(n == user.get("Name")) and bool(user.get("Password") == p) == True:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
