import numpy as np

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

        for i in range(len(sources)):
            if sources[i][0] <= loc and loc < sources[i][1]:
                rank = loc - sources[i][0]
                loc = destinations[i][0]+rank
                break
    if loc < res or res == -1:
        res = loc
print('res part 1 =', res)


l = len(seeds)//2
assert len(seeds)%2 == 0


def compute_intersection(interval1, intervals):
    res = []
    indices_intervals = []
    for I, inte in enumerate(intervals):
        b = max(interval1[0], inte[0])
        e = min(interval1[1], inte[1])
        if b<e or (interval1[0]==interval1[1]==b==e and inte[1]!=b):
            res.append([b, e])
            indices_intervals.append(I)
    return res, indices_intervals


def compute_intersection_complement(interval1, intervals):
    res = []
    for I, inte in enumerate(intervals):
        b = max(interval1[0], inte[0])
        e = min(interval1[1], inte[1])
        if b<=e:
            res.append([b, e])
    return res



def update_intervals(sources, sources_map, dests_map):


    temp, _ = compute_intersection([-1,100000000000000000], sources_map)
    temp = sorted(temp, key=lambda x: x[0])

    complement_sources_map = [[-1]]
    count = 0
    for te in temp:
        complement_sources_map[count].append(te[0])
        count += 1
        complement_sources_map.append([])
        complement_sources_map[count].append(te[1])
    complement_sources_map[count].append(100000000000000000)
    complement_sources_map = [interv for interv in complement_sources_map if interv[1]-interv[0]>0]

    split_sources = []
    split_sources_before = []
    for source in sources:
        intersect, indices_intervals = compute_intersection(source, sources_map)
        if len(intersect)>0:
            for inte, index_int in zip(intersect, indices_intervals):
                b = dests_map[index_int][0] + inte[0] - sources_map[index_int][0]
                e = dests_map[index_int][0] + inte[1] - sources_map[index_int][0]
                split_sources.append([b, e])
                split_sources_before.append(inte)

    split_sources_complement = []
    for source in sources:
        intersect = compute_intersection_complement(source, complement_sources_map)
        if len(intersect)>0:
            for inte in intersect:
                split_sources_complement.append(inte)

    return split_sources + split_sources_complement


locs = []

for J in range(l):

    b = seeds[2*J]
    e = b + seeds[2*J+1]

    locs.append([b,e])


def count_seeds(locs):
    count = 0
    for loc in locs:
        count += loc[1]-loc[0]
    return count

nbe_seeds = count_seeds(locs)



for cat, s_c in maps.items():
    sources_map = s_c[0]
    dests_map = s_c[1]

    locs = update_intervals(locs, sources_map, dests_map)

res = -1
for loc in locs:
    loc = np.array(loc)
    loc = loc[loc>0]
    if len(loc)>0 and (np.min(loc) < res or res == -1):
        res = np.min(loc)

print('res part 2 =', res)
