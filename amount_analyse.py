while True:
    amount = input("Enter an amount to analyze: ").strip()
    if amount.isnumeric():
        amount = int(amount)                # 123579
        #print(amount)
        d50 = amount // 50
        print("\t50.coin ==>", d50, "pc.")
        amount = amount % 50                # 29
        #print(amount)
        d20 = amount // 20
        print("\t20.coin ==>", d20, "pc.")
        amount = amount % 20                # 9
        #print(amount)
        d10 = amount // 10
        print("\t10.coin ==>", d10, "pc.")
        amount = amount % 10                # 9
        #print(amount)
        d5 = amount // 5
        print("\t 5.coin ==>", d5, "pc.")
        amount = amount % 5                 # 4
        #print(amount)
        d2 = amount // 2
        print("\t 2.coin ==>", d2, "pc.")
        amount = amount % 2                 # 0
        #print(amount)
        d1 = amount // 1
        print("\t 1.coin ==>", d1, "pc.\n")
    else:
        print("\n\tEnter a number!\n")
# INPUT
#       Enter an amount to analyze: 123579
# OUTPUT
#       50 coins ==> 2471 pc.
#       20 coins ==> 1 pc.
#       10 coins ==> 0 pc.
#       5 coins ==> 1 pc.
#       2 coins ==> 2 pc.
#       1 coins ==> 0 pc.