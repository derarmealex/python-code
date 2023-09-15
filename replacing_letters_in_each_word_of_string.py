# ALL OF 'A' WITH '#'
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
print(phrase.replace("A", "#"))                                         # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
# or
import re
print(re.sub('A+', '#', phrase))                                        # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
# or
exchanged = []
for letter in phrase:
    if letter != 'A':
        exchanged.append(letter)
    else:
        exchanged.append('#')
print("".join(exchanged))                                               # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
# or
print("".join([letter if letter != 'A' else '#' for letter in phrase])) # #BB#, #UTOM#TE, #BB#S, #BB#CY, #BB#TOIR
# THE FIRST X NUMBERS
phrase = "ABBA, AUTOMATE, ABBAS, ABBACY, ABBATOIR"
print(phrase.replace("A", "#", 2))                                      # #BB#, AUTOMATE, ABBAS, ABBACY, ABBATOIR
# or
import re
print(re.sub('A+', '#', phrase, 2))                                     # #BB#, AUTOMATE, ABBAS, ABBACY, ABBATOIR
# or
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
# ALL "#" INSTEAD OF "A" EXCEPT FOR THE FIRST
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
# ALL "#" INSTEAD OF "A" EXCEPT FOR THE SECOND (OR THE OTHER ONE)
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

# STRING WITHOUT ALL THE "T"
stg = "pythonist"

print(stg.replace('t', ''))                                                                    # pyhonis
# or
import re
print(re.sub('t+', '', stg))                                                                   # pyhonis
# or
final = []
for letter in stg:
    if letter != 't':
        final.append(letter)
print("".join(final))                                                                          # pyhonis
# or
print("".join(["" + letter for letter in stg if letter != 't']))                               # pyhonis
# or
print("".join(["" + stg[letter] for letter in range(len(stg)) if letter != 2 and letter != 8]))# pyhonis
# ONLY WITH THE FIRST ONE
stg = "pythonist"

final = ""
for letter in stg:
    if letter == 't' and 't' in final:
        continue
    else:
        final += letter
print(final)                                                                                   # pythonis
# or
print("".join(["" + stg[letter] for letter in range(len(stg)) if letter != 8]))                # pythonis
# ONLY WITHOUT THE FIRST ONE (or more)
stg = "pythonist"

print(stg.replace('t', '', 1)) #or more than 1                                                 # pyhonist
# or
import re
print(re.sub('t+', '', stg, 1))                                                                # pyhonist
# or
final = ""
count_t = 0
for letter in stg:
    if letter == 't' and count_t == 0:
        count_t += 1
        continue
    elif letter == 't' and count_t > 0:                                                        # or more than 0
        final += letter
    else:
        final += letter
print(final)                                                                                   # pyhonist
# or
final = ""
for letter in range(0, len(stg)):
    if letter != 2:
        final += stg[letter]
print(final)                                                                                   # pyhonist
# or
print("".join(["" + stg[letter] for letter in range(len(stg)) if letter != 2]))                # pyhonist
