# I
while True:
    word = str(input("Enter a value to check for palindrome: ")).strip().casefold()
    if word == word[::-1]:
        print("\tPalindrome\n")
    else:
        print("\tNot palindrome\n")
# II
while True:
    word = str(input("Enter a value to check for palindrome: ")).strip().casefold()
    if word == reversed(word):
        print("\tPalindrome\n")
    else:
        print("\tNot palindrome\n")
# III
while True:
    word = str(input("Enter a value to check for palindrome: ")).strip().casefold()
    x = len(word) - 1
    i = 0
    while x - i >= i:
        if word[x - i] == word[i]:
            i += 1
        else:
            print("\tNot paiindrome\n")
            break
        print("\tPalindrome\n")
        break
