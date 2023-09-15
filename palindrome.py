while True:
    word = str(input("Enter any value: ")).strip().casefold()
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
# or
while True:
    word = str(input("Enter any value: ")).strip().casefold()
    if word == reversed(word):
        print("Palindrome")
    else:
        print("Not palindrome")
# or
while True:
    word = str(input("Enter any value: ")).strip().casefold()
    x = len(word) - 1
    i = 0
    while x - i >= i:
        if word[x - i] == word[i]:
            i += 1
        else:
            print("Not paiindrome")
            break
        print("Palindrome")
        break
