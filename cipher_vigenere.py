# WITHOUT ORD(), CHR() FORMAT + REVERSE (LINE 3)
while True:
    word = input("Enter a word to cypher     (only letters): ")[::-1].lower().strip()
# 1: 'slovtso' ['ostvols']                  # 2: 'moribundus'  ['sudnubirom']
    pas  = input("Enter a password to cypher (only letters): ").lower().strip()
# 1: 'parolchik'                            # 2: 'code'
    if word.isalpha() and pas.isalpha():
        fit_pas = ''
# 1: parolch                                # 2: codecodeco
        while len(word) > len(fit_pas):
            for letter in pas:
                fit_pas += letter
        fit_pas = fit_pas[:len(word)]
#        print(fit_pas)
        abc = 'abcdefghijklmnopqrstuvwxyz'
        digit_move = []
# 1: [16, 1, 18, 15, 12, 3, 8]              # 2: [3, 15, 4, 5, 3, 15, 4, 5, 3, 15]
        for item in fit_pas:
            move = abc.find(item)
            digit_move.append(int(move) + 1)
#        print(digit_move)
        digit_word = []
# 1: [15, 19, 20, 22, 15, 12, 19]           # 2: [19, 21, 4, 14, 21, 2, 9, 18, 15, 13]
        for item in word:
            move = abc.find(item)
            digit_word.append(int(move) + 1)
#        print(digit_word)
        cipher = list(map(sum, zip(digit_word, digit_move)))
# 1: [31, 20, 38, 37, 27, 15, 27]           # 2: [22, 36, 8, 19, 24, 17, 13, 23, 18, 28]
#        print(cipher)
        final = []
        for item in cipher:
            item = item - 1
            if item > 25:
                item = abs(item - 26)
            final.append(abc[item])
        final = ''.join([letter for letter in final])
        print(
            f"\n  Precyphered     : {word}   \n"
            f"  Cyphered        : {final}    \n"
            f"  Cypher(password): {pas}      \n"
            )
# 1: Precyphered     : slovtso               # 2: Precyphered     : moribundus
##   Cyphered        : etlkaoa               ##   Cyphered        : vjhsxqmwrb
##   Cypher(password): parolchik             ##   Cypher(password): code
    else:
        print("\n Use only base letters! \n")
# STANDARD
while True:
    word = input("Enter a word to cypher     (only letters): ").lower().strip()
# 1: 'slovtso' ['ostvols']                  # 2: 'moribundus'  ['sudnubirom']
    pas  = input("Enter a password to cypher (only letters): ").lower().strip()
# 1: 'parolchik'                            # 2: 'code'
    if word.isalpha() and pas.isalpha():
        fit_pas = ""
# 1: parolch                                # 2: codecodeco
        while len(word) > len(fit_pas):
            for letter in pas:
                fit_pas += letter
        fit_pas = fit_pas[:len(word)]
#        print(fit_pas)
        dig_word = [ord(char) - 96 for char in word]
#1: [19, 12, 15, 22, 20, 19, 15]            # 2: [13, 15, 18, 9, 2, 21, 14, 4, 21, 19]
#        print(dig_word)
        dig_pas = [ord(char) - 96 for char in fit_pas]
# 1: [16, 1, 18, 15, 12, 3, 8]              # 2: [3, 15, 4, 5, 3, 15, 4, 5, 3, 15]
#        print(dig_pas)
        cipher = list(map(sum, zip(dig_word, dig_pas)))
        final = (''.join([chr(char + 96) if char + 96 < 123 else chr(char + 96 - 26) for char in cipher]))
        print(
                    f"\n  Precyphered     : {word}   \n"
                    f"  Cyphered        : {final}    \n"
                    f"  Cypher(password): {pas}      \n"
                    )
# 1: Precyphered     : slovtso               # 2: Precyphered     : moribundus
##   Cyphered        : imgkfvw               ##   Cyphered        : pdvnejrixh
##   Cypher(password): parolchik             ##   Cypher(password): code
    else:
        print("\n Use only base letters! \n")
