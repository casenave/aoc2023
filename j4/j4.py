import numpy as np
import re

with open('j4_input.txt') as f:
    input = f.readlines()


res = 0
for i, line in enumerate(input):
    sline = line.split("|")
    win_nums = sline[0].split(":")[1].strip().split(" ")
    cur_nums = sline[1].strip().split(" ")
    win_nums = [int(n) for n in win_nums if n != '']
    cur_nums = [int(n) for n in cur_nums if n != '']
    score = 0
    for n in cur_nums:
        if n in win_nums:
            if score == 0:
                score = 1
            else:
                score *= 2
    res += score

print('res part 1 =', res)

all_scratchcards = {}
for i in range(len(input)):
    all_scratchcards[i] = 1

for i, line in enumerate(input):
    sline = line.split("|")
    win_nums = sline[0].split(":")[1].strip().split(" ")
    cur_nums = sline[1].strip().split(" ")
    win_nums = [int(n) for n in win_nums if n != '']
    cur_nums = [int(n) for n in cur_nums if n != '']
    nb_wins = 0
    for n in cur_nums:
        if n in win_nums:
            nb_wins+=1
    for j in range(nb_wins):
        if j+i+1<len(input):
            all_scratchcards[j+i+1] += all_scratchcards[i]


res = 0
for i in range(len(input)):
    res += all_scratchcards[i]


print('res part 2 =', res)
    
