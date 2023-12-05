import numpy as np
from tqdm import tqdm

with open('j5_input.txt') as f:
    input = f.readlines()


seeds = [int(s) for s in input[0].split(": ")[1].split(" ")]

maps_init = {}
for inp in input[2:]:
    if inp[0] == '\n':
        continue
    elif inp[0].isdigit() == False:
        current_cat = inp.strip()[:-1]
        maps_init[current_cat] = []
    else:
        maps_init[current_cat].append([int(i) for i in inp.split(" ")])

maps = {}
max_origin = np.max(seeds)
for cat, vals in maps_init.items():
    sources = []
    destinations = []
    maps[cat] = {}
    for val in vals:
        sources.append([val[1], val[1]+val[2]])
        destinations.append([val[0], val[0]+val[2]])

    maps[cat]=(sources, destinations)

res = -1
for seed in seeds:
    loc = seed
    for cat, s_c in maps.items():
        sources = s_c[0]
        destinations = s_c[1]
        for i, source in enumerate(sources):
            if source[0] <= loc and loc < source[1]:
                rank = loc - source[0]
                loc = destinations[i][0]+rank
                break
    if loc < res or res == -1:
        res = loc
print('res part 1 =', res)