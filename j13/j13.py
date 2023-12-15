import numpy as np

with open('j13_input.txt') as f:
    input = f.readlines()


def init_patterns(input):
    indices = []
    for i, line in enumerate(input):
        if len(line)==1:
            indices.append(i)
    indices.append(len(input))

    i0 = 0
    patterns = []
    for i in indices:
        patterns.append(np.array([[c for c in input[j].strip()] for j in range(i0,i)], dtype = str))
        i0 = i+1
    return patterns
 
patterns = init_patterns(input)


def vertical_sym(pattern):
    nc = pattern.shape[1]
    res = []
    for j in range(1,nc):
        left = np.arange(j-1,-1,-1)
        right = np.arange(j,nc)
        bools = []
        for jj in range(min(len(left),len(right))):
            bools.append(pattern[:,left[jj]] == pattern[:,right[jj]])
        if np.all(bools):
            res.append(j)
    res = list(set(res))
    if len(res) == 0:
        return None
    else:
        return res


def horizontal_sym(pattern):
    nr = pattern.shape[0]
    res = []
    for i in range(1,nr):
        above = np.arange(i-1,-1,-1)
        below = np.arange(i,nr)
        bools = []
        for ii in range(min(len(above),len(below))):
            bools.append(pattern[above[ii],:] == pattern[below[ii],:])
        if np.all(bools):
            res.append(i)
    res = list(set(res))
    if len(res) == 0:
        return None
    else:
        return res

res_ = []
for I, pattern in enumerate(patterns):
    res_.append([])
    vs = vertical_sym(pattern)
    hs = horizontal_sym(pattern)
    if vs != None:
        for v in vs:
            res_[I].append(('v', v))
    if hs != None:
        for h in hs:
            res_[I].append(('h', h))

res = 0
for r in res_:
    assert len(r)==1
    if r[0][0] == 'v':
        res+=r[0][1]
    else:
        res+=100*r[0][1]

print('res part 1 =', res)


def flip_smudge(pattern, i, j):
    symb = pattern[i,j]
    if symb == ".":
        pattern[i,j] = "#"
    else:
        pattern[i,j] = "."


res = 0
for I, pattern in enumerate(patterns):
    prev_sym = res_[I]
    nr = pattern.shape[0]
    nc = pattern.shape[1]
    sym_found = False
    i = 0
    while i < nr and sym_found == False:
        j = 0
        while j < nc and sym_found == False:
            flip_smudge(pattern, i, j)
            vs = vertical_sym(pattern)
            hs = horizontal_sym(pattern)
            if vs != None:
                for v in vs:
                    if ('v',v) not in prev_sym:
                        sc = v
                        sym_found == True
            if hs != None:
                for h in hs:
                    if ('h',h) not in prev_sym:
                        sc = 100*h
                        sym_found == True
            flip_smudge(pattern, i, j)
            j += 1
        i += 1
    res += sc

print('res part 2 =', res)
    
