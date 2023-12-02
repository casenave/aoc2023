import numpy as np
import re

with open('j1_input.txt') as f:
    lines = f.readlines()

sum = 0
for l in lines:
    d = [int(s) for s in l.split()[0] if s.isdigit()]
    sum += d[0]*10+d[-1]

print("res part 1 =", sum)



words = ["zero", "one", "two", "three", "four",
"five", "six", "seven", "eight", "nine"]

invwords = [w[::-1] for w in words]


stop=False

sum = 0
for l in lines:
    string = l.split()[0]

    m = re.search(r"\d", string)
    rank1stdigit = m.start()

    replacerank = rank1stdigit
    replaceval  = ""

    for i, key in enumerate(words):
        rank = string.find(key)
        if rank < replacerank and rank>-1:
            replacerank = rank
            replaceval = key

    if replaceval != "":
        string = string.replace(replaceval, str(words.index(replaceval)), 1)

    invstring = string[::-1]

    m = re.search(r"\d", invstring)
    rank1stdigit = m.start()

    replacerank = rank1stdigit
    replaceval  = ""

    for i, key in enumerate(invwords):
        rank = invstring.find(key)
        if rank < replacerank and rank>-1:
            replacerank = rank
            replaceval = key

    if replaceval != "":
        invstring = invstring.replace(replaceval, str(invwords.index(replaceval)), 1)

    string = invstring[::-1]

    d = [int(s) for s in string if s.isdigit()]
    sum += d[0]*10+d[-1]

print("res part 2 =", sum)
