y = [',', 'J', 'm', 'f', 'x', 'U', '$', 'T', '>', 'q', "'", 'W', 'C', '!', '-', 'Y', '%', 'p', '_', 'P', 'A', 'i', 'Q', 'D', 's', 'E', 'u', '*', '^', 'v', '/', '{', 'e', ']', 'z', '(', ':', 'O', 'n', '|', 'F', 'w', ';', 'h', '<', 'H', 'a', 'M', '~', '+', 'd', '}', 't', 'G', 'R', 'g', 'y', '?', 'B', '=', 'L', 'S', 'Z', ')', '@', 'N', 'c', 'b', 'I', 'V', '&', 'r', 'X', '#', '.', 'j', 'o', 'l', 'k', '[', '`', 'K']
final = ''
while True:
    z = input('Enter a word without spaces and special characters: ')
    if z.isalpha():
        w = str(sum([12071992 + (ord(x)**7) for x in z]))
        count = 0
        while count < len(w):
            final += w[count] + y[count*2]
            count += 1
    else:
        print('Enter a word without spaces and special characters!'.upper())
    print(final)