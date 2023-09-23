a = 'lfydtd'
b = "12181"                                                     # moribundus
for x, y in zip(a, b): print(x + y, end='')                     # o0a4g0b6o0j0l1j0u1m1
"""
def pp(x):
    for ix, item in stg:
        if item in x:
            final.append(ix + move)


while True:
    move = 3
    stg = 'abcdefghijklmnopqrstuvwxyz'
    stg = enumerate(stg)
    final = []
    pp(input('Enter a word...  ').lower().strip())
    q = str(bytearray(final))
    print(q[len("bytearray(b'"):-2])
"""
# or
move = 3
abc = 'abcdefghijklmnopqrstuvwxyz'
abc = enumerate(abc)
while True:
    word = input('Enter a word...  ').lower().strip()           # 'moribundus'
    if word.isalpha():
        word_digit = []
        for ix, letter in abc:
            if letter in word:
                word_digit.append(ix + move)
#       print(word_digit)                                   # [4, 6, 11, 15, 16, 17, 20, 21, 23]
        cyph_word = str(bytearray(word_digit))
#       print(cyph_word)                                    # bytearray(b'\x04\x06\x0b\x0f\x10\x11\x14\x15\x17')
#       q = cyph_word[len("bytearray(b'"):-2]
#       print(q)                                            # \x04\x06\x0b\x0f\x10\x11\x14\x15\x17
        cyph_word = ''.join([num for num in cyph_word if num.isnumeric()])
        print(cyph_word)                                    # 0406001011141517
    else:
        print("\n\tUse only base letters!\n")
