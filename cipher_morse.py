# FROM ABC TO MORSE ABC
abc = "abcdefghijklmnopqrstuvwxyz"
morse_abc = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
while True:
    word = input("Enter a word to cypher in Morse code (only letters): ").lower().strip()
# 'leonardo'
    if word.isalpha():
        word_digit = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in word:
            ix = abc.find(letter)
            word_digit.append(int(ix))
#       print(word_digit)
        final = []
        for item in word_digit:
            final.append(morse_abc[item])
        final = ' '.join([letter for letter in final])
        print(
            f"\n  Precyphered : {word}\n"
            f"  Cyphered    : {final}\n"
            )
# Precyphered : leonardo
##Cyphered    : .-.. . --- -. .- .-. -.. ---
    else:
        print("\n Use only base letters! \n")

# FROM MORSE ABC TO ABC
abc = "abcdefghijklmnopqrstuvwxyz"
morse_abc = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
while True:
    word = input("Enter a word to cypher in Morse code (only letters): ").lower().strip()
# '.-.. . --- -. .- .-. -.. ---'
    word_split = word.split()
# ['.-..', '.', '---', '-.', '.-', '.-.', '-..', '---']
#       print(word_split)
    if set(morse_abc) | set(word_split) == set(morse_abc):
        word_digit = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in word_split:
            ix = morse_abc.index(letter)
            word_digit.append(int(ix))
#       print(word_digit)
        final = []
        for item in word_digit:
            final.append(abc[item])
        final = ''.join([letter for letter in final])
        print(
            f"\n  Precyphered : {word}\n"
            f"  Cyphered    : {final}\n"
            )
# Precyphered : .-.. . --- -. .- .-. -.. ---
##Cyphered    : leonardo
    else:
        print("\n Use only morse letters! \n")
