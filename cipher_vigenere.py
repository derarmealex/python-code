# WITHOUT ENCODING
while True:
    word = input("Enter a word to cypher     (only letters): ")[::-1].strip().lower()
    pas  = input("Enter a password to cypher (only letters): ").strip().lower()
    if word.isalpha() and pas.isalpha():
        pad_pas = ""
        while len(word) > len(pad_pas):
            for letter in pas:
                pad_pas += letter
        pad_pas = pad_pas[:len(word)]
        abc = "abcdefghijklmnopqrstuvwxyz"
        digit_move = []
        for item in pad_pas:
            move = abc.find(item)
            digit_move.append(int(move) + 1)
        digit_word = []
        for item in word:
            move = abc.find(item)
            digit_word.append(int(move) + 1)
        cipher = list(map(sum, zip(digit_word, digit_move)))
        final = []
        for item in cipher:
            item = item - 1
            if item > 25:
                item = abs(item - 26)
            final.append(abc[item])
        final = "".join([letter for letter in final])
        print(
            f"\n\tPrecyphered     : {word}\n"
            f"\tCyphered        : {final}\n"
            f"\tCypher(password): {pas}\n"
            )
    else:
        print("\n\tUse only base letters!\n")
# STANDARD
while True:
    word = input("Enter a word to cypher         (only letters): ").strip().lower()
    pas  = input("Enter a password for cyphering (only letters): ").strip().lower()
    if word.isalpha() and pas.isalpha():
        pad_pas = ""
        while len(word) > len(pad_pas):
            for letter in pas:
                pad_pas += letter
        pad_pas = pad_pas[:len(word)]
        digit_word = [ord(char) - 96 for char in word]
        digit_pas = [ord(char) - 96 for char in pad_pas]
        cipher = list(map(sum, zip(digit_word, digit_pas)))
        final = ("".join([chr(char + 96) if char + 96 < 123 else chr(char + 96 - 26) for char in cipher]))
        print(
                    f"\n\tPrecyphered     : {word}\n"
                    f"\tCyphered        : {final}\n"
                    f"\tCypher(password): {pas}\n"
                    )
    else:
        print("\n\tUse only base letters!\n")
