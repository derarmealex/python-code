while True:
    amount = input("Enter an amount to analyze: ").strip()
    if amount.isnumeric():
        amount = int(amount)                # 123579
        #print(amount)
        d50 = amount // 50
        print("\t50 cent ==>", d50, "pc.")
        amount = amount % 50                # 29
        #print(amount)
        d20 = amount // 20
        print("\t20 cent ==>", d20, "pc.")
        amount = amount % 20                # 9
        #print(amount)
        d10 = amount // 10
        print("\t10 cent ==>", d10, "pc.")
        amount = amount % 10                # 9
        #print(amount)
        d5 = amount // 5
        print("\t 5 cent ==>", d5, "pc.")
        amount = amount % 5                 # 4
        #print(amount)
        d2 = amount // 2
        print("\t 2 cent ==>", d2, "pc.")
        amount = amount % 2                 # 0
        #print(amount)
        d1 = amount // 1
        print("\t 1 cent ==>", d1, "pc.\n")
    else:
        print("\n\tEnter a number!\n")
# INPUT
#       Enter an amount to analyze: 123579
# OUTPUT
#       50 cent ==> 2471 pc.
#       20 cent ==> 1 pc.
#       10 cent ==> 0 pc.
#       5 cent ==> 1 pc.
#       2 cent ==> 2 pc.
#       1 cent ==> 0 pc.