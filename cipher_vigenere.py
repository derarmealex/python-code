while True:
    word = input("Enter a word to cypher     (only letters): ").lower().strip()
    pas  = input("Enter a password to cypher (only letters): ").lower().strip()
    if word.isalpha() and pas.isalpha():
        compr_pas = ''
        while len(word) > len(compr_pas):
            for letter in pas:
                compr_pas += letter
        compr_pas = compr_pas[:len(word)]
        abc = 'abcdefghijklmnopqrstuvwxyz'
        move_digit = []
        for item in compr_pas:
            move = abc.find(item)
            move_digit.append(int(move) + 1)
        new_word = []
        for item in word:
            move = abc.find(item)
            new_word.append(int(move) + 1)
        cipher = list(map(sum, zip(new_word, move_digit)))
        final = []
        for item in cipher:
            item = item - 1
            if item > 25:
                item = abs(item - 26)
            final.append(abc[item])
        print(''.join([x for x in final]), '\n')
    else:
        print("\nUse only letters!\n")
