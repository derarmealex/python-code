print('Summation:    "+",\nSubtraction:   "-",\n----------------------')
while True:
    oper = input("Choose the operation: ")
    if oper not in ('+','-'):
        print("Wrong operator. Try again.")
        continue
    else:
        ctr = True
        while ctr:
            num1 = input("Enter your first number: ")
            num2 = input("Enter your second number: ")
            if not num1.isnumeric() or not num2.isnumeric():
                print("Enter a number!")
                continue
            elif oper == "+":
                print(f"{int(num1)} + {int(num2)} = {int(num1) + int(num2)}")
            else:
                print(f"{int(num1)} - {int(num2)} = {int(num1) - int(num2)}")
            while True:
                goon = input("Like to do another operation?('y' for Yes, any other key for No): ").lower()
                if goon == 'y':
                    ctr = False
                    break
                else:
                    exit()
