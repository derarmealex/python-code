# FROM ABC TO MORSE ABC
abc = "abcdefghijklmnopqrstuvwxyz"
morse_abc = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
            ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            ]
while True:
    word = input("Enter a word to cypher in morse code (only letters): ").lower().strip()
# 'leonardo'
    if word.isalpha():
        digit_word = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in word:
            ix = abc.find(letter)
            digit_word.append(int(ix))
#       print(word_digit)
        final = []
        for item in digit_word:
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
    word = input("Enter a word in morse code to decipher (only morse letters): ").strip()
# '.-.. . --- -. .- .-. -.. ---'
    split_word = word.split()
# ['.-..', '.', '---', '-.', '.-', '.-.', '-..', '---']
#       print(split_word)
    if set(morse_abc) | set(split_word) == set(morse_abc):
        digit_word = []
# [11, 4, 14, 13, 0, 17, 3, 14]
        for letter in split_word:
            ix = morse_abc.index(letter)
            digit_word.append(int(ix))
#       print(digit_word)
        final = []
        for item in digit_word:
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
