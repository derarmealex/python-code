employees = {}
employee01 = {}
employee01.update({"Name": "Marek"})
employee01.update({"Surname": "Parek"})
employee01.update({"Email": "marek.parek@gmail.com"})
employees["employee01"] = employee01

employee02 = dict(Name="Matous", Surname="Svatous", Email="matous.svatous@gmail.com")
employees["employee02"] = employee02

employee03 = dict()
employee03["Name"] = "Anna"
employee03["Surname"] = "Rana"
employee03["Email"] = "anna.rana@gmail.com"
employees["employee03"] = employee03

print("All the keys:", employees.keys())
print("All the values:", employees.values())
print("All the details to the last employee:", employees["employee03"].items())

input()