# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = 82.0
collection = []
main_ctr = True
while main_ctr:
    try:
        num = float(input("Enter [next] number to calculate: "))
        print("")
    except ValueError:
        print(f"\n\tIncorrect number! Try again")
        print("\tYour collection to process now:", collection)
        continue
    else:
        collection.append(num)
        while True:
            print("\tYour collection to process:", collection, "")
            oper = input(
                        'Summation     : "+"\n'
                        'Subtraction   : "-"\n'
                        'Multiplication: "*"\n'
                        'Division      : "/"\n'
                        'Exponentiation: "^"\n'
                        '-------------------\n'
                        "Select operator, or print 'start' to break input and start calculating: "
                        ).strip().lower()
            print("")
            if oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "^":
                collection.append(oper)
                print("\tYour collection to process now:", collection, "\n")
                break
            elif oper == "start":
                main_ctr = False
                break
            else:
                print(f"\tWrong operator! --> ({oper}) <-- Try again")
fin_col = " ".join([str(x) for x in collection])
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0
print(fin_col)
col = collection
index_move = 0
if "^" in col:
    for ix, item in enumerate(col):
        if item == "^":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            pow_res = num1 ** num2
            col[ix - 1] = pow_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "/" in col:
    for ix, item in enumerate(col):
        if item == "/":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            try:
                div_res = num1 / num2
            except ZeroDivisionError:
                print("\n\tCouldn't be divided by 0! Expression has no solution\n")
                exit()
            col[ix - 1] = div_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "*" in col:
    for ix, item in enumerate(col):
        if item == "*":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            mult_res = num1 * num2
            col[ix - 1] = mult_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "-" in col:
    for ix, item in enumerate(col):
        if item == "-":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            sub_res = num1 - num2
            col[ix - 1] = sub_res
            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
index_move = 0
if "+" in col:
    for ix, item in enumerate(col):
        if item == "+":
            ix -= index_move
            num1 = col[ix - 1]
            num2 = col[ix + 1]
            sum_res = num1 + num2
            col[ix - 1] = sum_res

            temp_slice = col[:ix]
            temp_slice2 = col[ix + 2:]
            col = temp_slice + temp_slice2
            index_move += 2
result = col[0]
print(f"\n\t{fin_col} = {result}\n")
# 9.0 ^ 2.0 + 1 - 3.5 * 0.0 / 2.0 ^ 5.0 * 7.0 * 10.0 = 82.0
