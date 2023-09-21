while True:
    word = input("Enter a word to cypher     (only letters): ")[::-1].lower().strip()
# 1: 'slovtso' ['ostvols']                  # 2: 'moribundus'  ['sudnubirom']
    pas  = input("Enter a password to cypher (only letters): ").lower().strip()
# 1: 'parolchik'                            # 2: 'code'
    if word.isalpha() and pas.isalpha():
        fit_pas = ''
        while len(word) > len(fit_pas):
            for letter in pas:
                fit_pas += letter
        fit_pas = fit_pas[:len(word)]
#        print(fit_pas)
# 1: parolch                                # 2: codecodeco
        abc = 'abcdefghijklmnopqrstuvwxyz'
        move_digit = []
        for item in fit_pas:
            move = abc.find(item)
            move_digit.append(int(move) + 1)
#        print(move_digit)
# 1: [16, 1, 18, 15, 12, 3, 8]              # 2: [3, 15, 4, 5, 3, 15, 4, 5, 3, 15]
        word_digit = []
        for item in word:
            move = abc.find(item)
            word_digit.append(int(move) + 1)
#        print(word_digit)
# 1: [15, 19, 20, 22, 15, 12, 19]           # 2: [19, 21, 4, 14, 21, 2, 9, 18, 15, 13]
        cipher = list(map(sum, zip(word_digit, move_digit)))
#        print(cipher)
# 1: [31, 20, 38, 37, 27, 15, 27]           # 2: [22, 36, 8, 19, 24, 17, 13, 23, 18, 28]
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
# 1: etlkaoa                                # 2: vjhsxqmwrb
    else:
        print("\n Use only base letters! \n")
