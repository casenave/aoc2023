

with open('j11_input.txt') as f:
    input0 = f.readlines()

input = []
for inp in input0:
    input.append(inp.strip())

h = len(input)
w = len(input[0])

import numpy as np
map = np.zeros((h, w), dtype=str)
for i in range(h):
    for j in range(w):
        map[i,j] = input[i][j]
        

rows_to_expand = []
for i in range(h):
    if len(map[i][map[i]=="."]) == w:
        rows_to_expand.append(i)
cols_to_expand = []
for j in range(w):
    if len(map[:,j][map[:,j]=="."]) == h:
        cols_to_expand.append(j)


extended_map_rows = np.zeros((h+len(rows_to_expand), w), dtype=str)
count = 0
prev = 0
for i in rows_to_expand:
    extended_map_rows[prev+count:count+i,:] = map[prev:i,:]
    extended_map_rows[i+count,:] = ['.' for _ in range(w)]
    prev = i
    count += 1
extended_map_rows[prev+count:count+h,:] = map[prev:h,:]


extended_map = np.zeros((h+len(rows_to_expand), w+len(cols_to_expand)), dtype=str)
count = 0
prev = 0
for j in cols_to_expand:
    extended_map[:,prev+count:count+j] = extended_map_rows[:,prev:j]
    extended_map[:,j+count] = ['.' for _ in range(h+len(rows_to_expand))]
    prev = j
    count += 1
extended_map[:,prev+count:count+w+len(cols_to_expand)] = extended_map_rows[:,prev:w+len(cols_to_expand)]


h2 = h+len(rows_to_expand)
w2 = w+len(cols_to_expand)

count = 1
location_galaxies = []
for i in range(h2):
    for j in range(w2):
        if extended_map[i,j] == '#':
            extended_map[i,j] = str(count)
            count += 1
            location_galaxies.append((i,j))

n_galaxies = len(location_galaxies)


def dist(p1, p2):
    return np.abs(p2[0]-p1[0])+np.abs(p2[1]-p1[1])

n_pairs = 0
distances = [] 
for I in range(n_galaxies):
    for J in range(I):
        n_pairs += 1
        distances.append(dist(location_galaxies[I], location_galaxies[J]))

print('res part 1 =', np.sum(distances))

######



count = 1
location_galaxies = []
for i in range(h):
    for j in range(w):
        if map[i,j] == '#':
            map[i,j] = str(count)
            count += 1
            location_galaxies.append((i,j))

# print("location_galaxies =", location_galaxies)
# print("rows_to_expand =", rows_to_expand)
# print("cols_to_expand =", cols_to_expand)


def rank_in(n, list):
    for i, m in enumerate(list):
        assert n!=m
        if m>n:
            return i
    return i+1

dil = 1e6-1

n_galaxies = len(location_galaxies)
for I in range(n_galaxies):
    x = location_galaxies[I][0]
    y = location_galaxies[I][1]
    x_d = rank_in(x, rows_to_expand)
    y_d = rank_in(y, cols_to_expand)
    location_galaxies[I] = (x+dil*x_d, y+dil*y_d)


distances = [] 
for I in range(n_galaxies):
    for J in range(I):
        distances.append(dist(location_galaxies[I], location_galaxies[J]))
        dd = dist(location_galaxies[I], location_galaxies[J])

print('res part 2 =', int(np.sum(distances)))
    
