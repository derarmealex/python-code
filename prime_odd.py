def find_prime(seq):
    for i in seq:
        if i > 1:
            ctr = 2
            while ctr < i:
                y = i % ctr
                ctr += 1
                if y == 0:
                    break
            else:
                yield i
        else:
            continue


def find_odd_prime(seq):
    for num in seq:
        if num % 2 != 0:
            yield num


a_pipeline = find_odd_prime(find_prime([1, 2, 3, 4, 17, 47, 50, 90, 101, 0]))
print(list(a_pipeline))                 # [3, 17, 47, 101]
# or
for a_ele in a_pipeline:
    print(a_ele, end=" ")               # 3 17 47 101
