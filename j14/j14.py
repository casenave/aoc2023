import numpy as np

with open('j14_input.txt') as f:
    input = f.readlines()


def init_platform(input):
    return np.array([[c for c in line.strip()] for line in input], dtype = str)

platform = init_platform(input)

nr = platform.shape[0]
nc = platform.shape[1]


def tilt(platform):
    for j in range(nc):
        O_loc = np.arange(nr)[platform[:,j]=='O']
        C_loc = np.arange(nr)[platform[:,j]=='#']
        for O_r in O_loc:
            northern_indices = np.arange(O_r)
            free_spaces = northern_indices[platform[northern_indices,j]=='.']
            C_loc_local = C_loc[C_loc<O_r]
            if len(C_loc_local>0):
                free_spaces = free_spaces[free_spaces>C_loc_local[-1]]
            if len(free_spaces)>0:
                platform[free_spaces[0],j] = 'O'
                platform[O_r,j] = '.'
    return platform


def compute_load(platform):
    res = 0
    for i in range(nr):
        res += (nr-i)*len(platform[i,platform[i,:]=='O'])
    return res

tilt(platform)

print('res part 1 =', compute_load(platform))



def rotate_90_deg(platform):
    return platform.T[::-1,:]

def rotate_neg90_deg(platform):
    return platform.T[:,::-1]


def rotate_180_deg(platform):
    return platform[::-1,::-1]


def cycle(platform):

    platform = tilt(platform)

    platform = rotate_neg90_deg(platform)
    platform = tilt(platform)
    platform = rotate_90_deg(platform)

    platform = rotate_180_deg(platform)
    platform = tilt(platform)
    platform = rotate_180_deg(platform)

    platform = rotate_90_deg(platform)
    platform = tilt(platform)
    platform = rotate_neg90_deg(platform)

    return platform




platform = init_platform(input)

def compute_location_0(platform):
    l0_i = []
    l0_j = []
    for i in range(nr):
        for j in range(nc):
            if platform[i,j] == "O":
                l0_i.append(i)
                l0_j.append(j)
    return np.array([l0_i, l0_j])

l0_init = compute_location_0(platform)


nb_cycles = 1000000000

all_l0 = [l0_init]


count = 1
found_cycle = False
while count <nb_cycles and found_cycle == False:
    platform = cycle(platform)
    l0 = compute_location_0(platform)
    for I, l in enumerate(all_l0):
        if np.linalg.norm(l0-l) == 0:
            found_cycle = True
            transit = I
    all_l0.append(l0)
    count += 1

loop_length = len(all_l0)-1-transit
nb_red = transit + (nb_cycles-transit)%loop_length

platform = init_platform(input)
for _ in range(nb_red):
    platform = cycle(platform)

print('res part 2 =', compute_load(platform))