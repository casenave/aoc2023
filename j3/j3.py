

with open("j3_input.txt") as f:
    input = f.readlines()

symbols=["%", "-", "#", "=", "*", "+", "=", "&", "/", "@", "$"]

import re
import numpy as np


max_lines = len(input)
max_col = len(input[0])


numbers = []
rows = []
columns = []

count = 0
for i, line in enumerate(input):
    for m in re.finditer(r'\d+', line):
        s = m.start()
        e = m.end()
        v = m.group(0)

        rows.append([])
        columns.append([])

        if i>0:
            rows[count].append(i-1)
        rows[count].append(i)
        if i<max_lines-1:
            rows[count].append(i+1)

        if s>0:
            columns[count].append(s-1)
        for c in range(s, e):
            columns[count].append(c)
        if s<max_col-1:
            columns[count].append(e)
        
        numbers.append(int(v))

        count+=1

res = 0
possibles = []
for i, n in enumerate(numbers):
    possible = False
    for r in rows[i]:
        for c in columns[i]:
            for s in symbols:
                if s == input[r][c]:
                    possible = True
    if possible == True:
        res += n
    possibles.append(possible)

print("res part 1 =", res)




res = 0

stars_rows = []
stars_columns = []

star_id_to_numbers_rank = {}
for i, n in enumerate(numbers):
    for r in rows[i]:
        for c in columns[i]:
            if input[r][c] == "*":
                if (r,c) in star_id_to_numbers_rank:
                    star_id_to_numbers_rank[(r,c)].append(i)
                else:
                    star_id_to_numbers_rank[(r,c)]=[i]


res = 0
for number_ids in star_id_to_numbers_rank.values():
    if len(number_ids) == 2:
        res += numbers[number_ids[0]]*numbers[number_ids[1]]


print("res part 2 =", res)