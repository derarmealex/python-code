while True:
    print("Enter any value: ")
    word = str(input().casefold())
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
#or
while True:
    print("Enter any value: ")
    word = str(input().casefold())
    if word == reversed(word):
        print("Palindrome")
    else:
        print("Not palindrome")
#or
while True:
    val = str(input("Enter any value: "))
    x = len(val)
    x = x - 1
    i = 0
    k = 0
    while x - i >= i:
        if val[x - i] == val[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        print("Not paiindrome")
    else:
        print("Palindrome")