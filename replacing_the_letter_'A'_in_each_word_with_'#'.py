#ALL OF THEM
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
print(phrase.replace("A", "#"))                                         # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
#or
import re
print(re.sub('A+', '#', phrase))                                        # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
#or
exchanged = []
for letter in phrase:
    if letter != 'A':
        exchanged.append(letter)
    else:
        exchanged.append('#')
print("".join(exchanged))                                               # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
#or                                                                    
print("".join([letter if letter != 'A' else '#' for letter in phrase])) # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
#THE FIRST X NUMBERS
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
print(phrase.replace("A", "#", 2))                                      # #BB#, AUTOMATE, ABBAS, ABBACY, ABBATOIR
#or
import re
print(re.sub('A+', '#', phrase, 2))                                     # #BB#, AUTOMATE, ABBAS, ABBACY, ABBATOIR
#or
exchanged = ""
count_a = 0
for letter in phrase:
    if letter != 'A':
        exchanged += letter
    elif letter == 'A' and count_a > 1:
        exchanged += letter
    else:
        exchanged += '#'
        count_a += 1
print(exchanged)                                                        # #BB#, AUTOMATE, ABBAS, ABBACY, ABBATOIR
#ALL "#" INSTEAD OF "A" EXCEPT FOR THE FIRST
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
exchanged = ""
count_a = 0
for letter in phrase:
    if letter != 'A':
        exchanged += letter
    elif letter == 'A' and count_a != 0:
        exchanged += '#'
        continue
    else:
        exchanged += letter
        count_a += 1
print(exchanged)                                                        # ABB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
#ALL "#" INSTEAD OF "A" EXCEPT FOR THE SECOND (OR THE OTHER ONE)
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
exchanged = ""
count_a = 0
for letter in phrase:
    if letter != 'A':
        exchanged += letter
    elif letter == 'A' and count_a != 1:                                # replace for any other number
        exchanged += '#'
        count_a += 1
        continue
    else:
        exchanged += letter
        count_a += 1
print(exchanged)                                                        # #BBA, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR