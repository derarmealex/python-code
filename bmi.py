# I
while True:
    try:
        m = float(input("Enter mass of body in kg   : "))
        h = float(input("Enter height of body in cm : "))
    except ValueError:
        print("\n\tEnter a correct number!\n")
    else:
        try:
            calc = round(m / (h / 100)**2, 2)
        except ZeroDivisionError:
            print("\n\tCouldn't be divided by 0! Enter a correct number\n")
        else:
            print("\n\tBMI is:", calc)
            if calc <= 16.0:
                print("\tIt's underweight (severe thinness)\n")
            elif 16.0 < calc < 16.9:
                print("\tIt's underweight (moderate thinness)\n")
            elif 17.0 < calc < 18.4:
                print("\tIt's underweight (mild thinness)\n")
            elif 18.5 < calc < 24.9:
                print("\tIt's a normal range\n")
            elif 25.0 < calc < 29.9:
                print("\tIt's overweight (pre-obese)\n")
            elif 30.0 < calc < 34.9:
                print("\tIt's obese (class I)\n")
            elif 35.0 < calc < 39.9:
                print("\tIt's obese (class II)\n")
            elif calc >= 40.0:
                print("\tIt's obese (class III)\n")
# II
from re import findall
while True:
    m = input("Enter mass of body in kg   : ").strip()
    h = input("Enter height of body in cm : ").strip()
    if findall('[^.\d]', m) or findall('[^.\d]', h) \
            or m == '0' or h == '0' \
            or m == '.' or h == '.' \
            or m in '' or h in '':
        print("\n\tEnter a correct number!\n")
    else:
        calc = round(float(m) / (float(h) / 100)**2, 2)
        print("\n\tBMI is:", calc)
        if calc <= 16.0:
            print("\tIt's underweight (severe thinness)\n")
        elif 16.0 < calc < 16.9:
            print("\tIt's underweight (moderate thinness)\n")
        elif 17.0 < calc < 18.4:
            print("\tIt's underweight (mild thinness)\n")
        elif 18.5 < calc < 24.9:
            print("\tIt's a normal range\n")
        elif 25.0 < calc < 29.9:
            print("\tIt's overweight (pre-obese)\n")
        elif 30.0 < calc < 34.9:
            print("\tIt's obese (class I)\n")
        elif 35.0 < calc < 39.9:
            print("\tIt's obese (class II)\n")
        elif calc >= 40.0:
            print("\tIt's obese (class III)\n")
# INPUT
#       Enter mass of body in kg   : 90
#       Enter height of body in cm : 180
# OUTPUT
#       BMI is: 27.78
#       It's overweight (pre-obese)
