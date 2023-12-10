

with open('j10_input.txt') as f:
    input = f.readlines()


directions = {'|':((-1,0),(1,0)), '-':((0,-1),(0,1)), 'L':((-1,0),(0,1)), 'J':((-1,0),(0,-1)), '7':((0,-1),(1,0)), 'F':((1,0),(0,1))}
directions['S'] = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


map = []
for line in input:
    map.append([s for s in line.strip()])


import numpy as np
def admissible_indices(i, j):

    i_s = np.array([i-1, i, i+1])
    i_s = i_s[i_s>=0]
    i_s = i_s[i_s<len(map)]

    j_s = np.array([j-1, j, j+1])
    j_s = j_s[j_s>=0]
    j_s = j_s[j_s<len(map[0])]

    indices = []
    for i_ in i_s:
        for j_ in j_s:
            indices.append((i_,j_))
    indices.remove((i,j))
    return indices

def connections(i, j):
    connect = []
    ad_ind = admissible_indices(i, j)
    symbol = map[i][j]
    dirs = [(i+directions[symbol][k][0],j+directions[symbol][k][1]) for k in range(len(directions[symbol]))]
    for index in dirs:
        if index in ad_ind and map[index[0]][index[1]] in directions:
           connect.append(index) 
    return connect

def next_connection(prev_i, prev_j, i, j):
    connect = connections(i, j)
    if (prev_i, prev_j) == connect[0]:
        return connect[1]
    elif (prev_i, prev_j) == connect[1]:
        return connect[0]
    else:
        raise

start = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'S':
            start.append((i,j))
assert len(start) == 1
start = start[0]

start_connections = [conn for conn in connections(start[0], start[1]) if start in connections(conn[0], conn[1])]


loops = []
for start_c in start_connections:
    loop = [start, start_c]
    while True:
        connect = [conn for conn in connections(loop[-1][0], loop[-1][1]) if loop[-1] in connections(conn[0], conn[1])]
        assert len(connect) == 2
        if loop[-2] == connect[0]:
            next = connect[1]
        elif loop[-2] == connect[1]:
            next = connect[0]
        else:
           raise
        loop.append(next)
        
        if next == start:
            break
    loops.append(loop)

l = len(loops[0])

print('res part 1 =', int(l/2))



def print_m(map):
    string_ =""
    for line in map:
        string_ += "".join(line)+str("\n")
    print(string_)


def count_(val, map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == val:
                count += 1
    return count


loop = loops[1]
xl = [l[0] for l in loop]
yl = [l[1] for l in loop]
bbox = [(min(xl), min(yl)), (max(xl), max(yl))]

nx = len(map)
ny = len(map[0])

potential_nest = []
for i in range(nx):
    for j in range(ny):
        if min(xl)<=i and i<max(xl) and min(yl)<=j and j<max(yl) and (i,j) not in loop:
            potential_nest.append((i,j))
            map[i][j] = "H"
        if min(xl)>i or i>=max(xl) or min(yl)>j or j>=max(yl):
            map[i][j] = "H"

map[start[0]][start[1]] = "|"

res = 0
for p in potential_nest:
    x1 = np.arange(0, p[0])
    x2 = np.arange(p[0]+1, nx)
    mx1 = [map[x][p[1]] for x in x1]
    mx2 = [map[x][p[1]] for x in x2]

    if mx1.count("H") == len(mx1) or mx1.count("H") == len(mx2):
        map[p[0]][p[1]] = "O"
        continue

    mx1 = "".join(mx1)
    mx2 = "".join(mx2)
    mx1 = mx1.replace("|", "")
    mx2 = mx2.replace("|", "")
    for s in ["FL", "LF", "7J", "J7"]:
        mx1 = mx1.replace(s, "")
        mx2 = mx2.replace(s, "")
    for s in ["7L", "L7", "FJ", "JF"]:
        mx1 = mx1.replace(s, "-")
        mx2 = mx2.replace(s, "-")        

    n = mx1.count("-")
    if n%2==1:
        res += 1
        map[p[0]][p[1]] = "I"
    else:
        map[p[0]][p[1]] = "O"

print('res part 2 =', res)

print_m(map)
