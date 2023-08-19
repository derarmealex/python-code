while True:
    m = (input("Enter mass of body in kg: "))
    h = (input("Enter height of body in cm: "))
    if m.isnumeric() and h.isnumeric():
        calc = round(int(m) / (int(h)/100)**2, 2)
        print("BMI is:", calc)
        if calc <= 16.0:
            print("It's underweight (severe thinness)\n")
        elif 16.0 < calc < 16.9:
            print("It's underweight (moderate thinness)\n")
        elif 17.0 < calc < 18.4:
            print("It's underweight (mild thinness)\n")
        elif 18.5 < calc < 24.9:
            print("It's a normal range\n")
        elif 25.0 < calc < 29.9:
            print("It's overweight (pre-obese)\n")
        elif 30.0 < calc < 34.9:
            print("It's obese (class I)\n")
        elif 35.0 < calc < 39.9:
            print("It's obese (class I)\n")
        elif calc >= 40.0:
            print("It's obese (class I)\n")
    elif '.' in m or '.' in h:
        calc = round(float(m) / (float(h)/100)**2, 2)
        print("BMI is:", calc)
        if calc <= 16.0:
            print("It's underweight (severe thinness)\n")
        elif 16.0 < calc < 16.9:
            print("It's underweight (moderate thinness)\n")
        elif 17.0 < calc < 18.4:
            print("It's underweight (mild thinness)\n")
        elif 18.5 < calc < 24.9:
            print("It's a normal range\n")
        elif 25.0 < calc < 29.9:
            print("It's overweight (pre-obese)\n")
        elif 30.0 < calc < 34.9:
            print("It's obese (class I)\n")
        elif 35.0 < calc < 39.9:
            print("It's obese (class I)\n")
        elif calc >= 40.0:
            print("It's obese (class I)\n")
    else:
        print("\nEnter an integer or fractional number!".upper())
