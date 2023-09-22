while True:
    nums_to_sum = input("Enter a number to calculate sum of its digits: ").strip()  # 99999
    if nums_to_sum.isnumeric():
        final = sum([0 + int(num) for num in nums_to_sum])
        print(f'Number: {nums_to_sum} |==> Sum of its digits: {final}')             # Number: 99999 |==> Sum of its digits: 45
    else:
        print("Enter a correct number!")
