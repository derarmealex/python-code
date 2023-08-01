# converse Lb to kg
repeat = True
while repeat:
    Lb = input("Enter libres:\n")
    if Lb.isnumeric():
        print(Lb, "Lb is", round(int(Lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_Lb = input("Do you have another value for measure? y/n\n")
        if another_Lb == "y":
            repeat = True
        elif another_Lb == "n":
            pass
        else:
            pass
    elif "." in Lb:
        print(Lb, "Lb is", round(float(Lb)/2.2, 2), "kg", "\n")
        repeat = False
        another_Lb = input("Do you have another value for measure? y/n\n")
        if another_Lb == "y":
            repeat = True
        elif another_Lb == "n":
            pass
        else:
            pass
    else:
        print("Wrong value, enter a number")
    
# converse mile to km
print("Enter miles:")
mile = float(input())
print(mile, "mile is", round(mile/0.62, 2), "km", "\n")

# converse gal to l
print("Enter gallons:")
gal = float(input())
print(gal, "gal is", round(gal/0.26, 2), "l", "\n")

input()
