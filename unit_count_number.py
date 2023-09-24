while True:
    num_to_ctr = input("Enter a number to count units: ")[::-1].strip()
# 123579 --> 975321
    if num_to_ctr.isnumeric():
        count = {}
        for ix, unit in enumerate(num_to_ctr):
            dict_key = "1" + ("0" * ix)
            count[dict_key] = unit
#        print(count)
        for key, value in count.items():
            output_space = len(num_to_ctr) - len(key) + 1
            print("\t^" + key + " "*output_space + "u-*>:", value)
#            print(f"\t^{key}{' '*output_space}u-*>: {value}")
        print("")
    else:
        print("\n\tEnter a number!\n")
# or
while True:
    num_to_ctr = input("Enter a number to count units: ").strip()
# 123579
    if num_to_ctr.isnumeric():
        num_len = len(num_to_ctr)
        num_to_ctr = int(num_to_ctr)
        count = {}
        for step in range(num_len):
            unit = num_to_ctr % 10
            dict_key = "1" + ("0" * step)
            count[dict_key] = unit
            next_step = num_to_ctr // 10
            num_to_ctr = next_step
#        print(count)
        for key, value in count.items():
            output_space = num_len - len(key) + 1
#            print("\t^" + key + " "*output_space + "u-*>:", value)
            print(f"\t^{key}{' '*output_space}u-*>: {value}")
        print("")
    else:
        print("\n\tEnter a number!\n")
# INPUT
#       Enter a number to count units: 123579
# OUTPUT
#       {'1': '9', '10': '7', '100': '5', '1000': '3', '10000': '2', '100000': '1'}
# or
#       ^1      u-*>: 9
#       ^10     u-*>: 7
#       ^100    u-*>: 5
#       ^1000   u-*>: 3
#       ^10000  u-*>: 2
#       ^100000 u-*>: 1