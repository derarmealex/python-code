# FROM ABC TO MORSE ABC <==> FROM MORSE ABC TO ABC
abc = "abcdefghijklmnopqrstuvwxyz"
morse_abc = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
while True:
    word = input(
                "Enter a word to cypher in morse code (only letters), or \n"
                "enter a word in morse code to decipher (only morse letters): "
                ).lower().strip()
    split_word = word.split()                                   # for converting to regular ABC
    if word.isalpha():
# 'leonardo'
        digit_word = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in word:
            ix = abc.find(letter)
            digit_word.append(int(ix))
#       print(word_digit)
        final = []
        for item in digit_word:
            final.append(morse_abc[item])
        final = " ".join([letter for letter in final])
        print(
            f"\n\tPrecyphered : {word}\n"
            f"\tCyphered    : {final}\n"
            )
# INPUT
#       Enter a word to cypher in morse code (only letters), or
#       enter a word in morse code to decipher (only morse letters): leonardo
# OUTPUT
#       Precyphered : leonardo
#       Cyphered    : .-.. . --- -. .- .-. -.. ---
    elif set(morse_abc) | set(split_word) == set(morse_abc):    # if there's only morse letters in the word
# '.-.. . --- -. .- .-. -.. ---
        split_word = word.split()
        digit_word = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in split_word:
            ix = morse_abc.index(letter)
            digit_word.append(int(ix))
#       print(digit_word)
        final = []
        for item in digit_word:
            final.append(abc[item])
        final = "".join([letter for letter in final])
        print(
            f"\n\tPrecyphered : {word}\n"
            f"\tCyphered    : {final}\n"
        )
# INPUT
#       Enter a word to cypher in morse code (only letters), or
#       enter a word in morse code to decipher (only morse letters): .-.. . --- -. .- .-. -.. ---
# OUTPUT
#       Precyphered : .-.. . --- -. .- .-. -.. ---
#       Cyphered    : leonardo
    else:
        print("\n\tUse only base letters, or only morse characters!\n")
