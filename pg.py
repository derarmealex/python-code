a = ""
b = ""
for x, y in zip(a, b): print(x + y, end='')
"""
def pp(x):
    for ix, item in stg:
        if item in x:
            final.append(ix + move)


while True:
    move = 
    stg = 'abcdefghijklmnopqrstuvwxyz'
    stg = enumerate(stg)
    final = []
    pp(input('Enter a word...  ').lower().strip())
    q = str(bytearray(final))
    print(q[len("bytearray(b'"):-2])
"""
# or
move = 
abc = 'abcdefghijklmnopqrstuvwxyz'
abc = enumerate(abc)
while True:
    word = input('Enter a word...  ').lower().strip()
    if word.isalpha():
        word_digit = []
        for ix, letter in abc:
            if letter in word:
                word_digit.append(ix + move)
#       print(word_digit)
        cyph_word = str(bytearray(word_digit))
#       print(cyph_word)
#       q = cyph_word[len("bytearray(b'"):-2]
#       print(q)
        cyph_word = ''.join([num for num in cyph_word if num.isnumeric()])
        print(cyph_word)
    else:
        print("\n\tUse only base letters!\n")
