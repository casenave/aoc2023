import numpy as np

with open('j16_input.txt') as f:
    input = f.readlines()


def init_platform(input):
    return np.array([[c for c in line.strip()] for line in input], dtype = str)


platform = init_platform(input)

nr = platform.shape[0]
nc = platform.shape[1]

def print_p(platform):
    string_ = ""
    for row in platform:
        string_ += "".join(row)+"\n"
    print(string_)


tile_behavior = {'.':{}, '/':{}, '\\':{}, '-':{}, '|':{}}

tile_behavior['.']['>'] = [(0,1,'>')]
tile_behavior['.']['<'] = [(0,-1,'<')]
tile_behavior['.']['^'] = [(-1,0,'^')]
tile_behavior['.']['v'] = [(1,0,'v')]

tile_behavior['/']['>'] = [(-1,0,'^')]
tile_behavior['/']['<'] = [(1,0,'v')]
tile_behavior['/']['^'] = [(0,1,'>')]
tile_behavior['/']['v'] = [(0,-1,'<')]

tile_behavior['\\']['>'] = [(1,0,'v')]
tile_behavior['\\']['<'] = [(-1,0,'^')]
tile_behavior['\\']['^'] = [(0,-1,'<')]
tile_behavior['\\']['v'] = [(0,1,'>')]

tile_behavior['-']['>'] = [(0,1,'>')]
tile_behavior['-']['<'] = [(0,-1,'<')]
tile_behavior['-']['^'] = [(0,-1,'<'),(0,1,'>')]
tile_behavior['-']['v'] = [(0,-1,'<'),(0,1,'>')]

tile_behavior['|']['>'] = [(-1,0,'^'),(1,0,'v')]
tile_behavior['|']['<'] = [(-1,0,'^'),(1,0,'v')]
tile_behavior['|']['^'] = [(-1,0,'^')]
tile_behavior['|']['v'] = [(1,0,'v')]



def propagate(platform, i, j, direction, beam_tracking = None):

    if beam_tracking == None:
        beam_tracking = {}

    while 0<=i<nr and 0<=j<nc:

        if (i,j) not in beam_tracking:
            beam_tracking[(i,j)] = []
        
        if direction in beam_tracking[(i,j)]:
            break

        beam_tracking[(i,j)].append(direction)

        nexts = tile_behavior[platform[i,j]][direction]

        if len(nexts)==2:
            propagate(platform, i+nexts[1][0], j+nexts[1][1], nexts[1][2], beam_tracking)

        i+=nexts[0][0]
        j+=nexts[0][1]
        direction=nexts[0][2]
        
    return beam_tracking

beam_tracking = propagate(platform, 0, 0, ">")

def energize(beam_tracking, platform):
    plat = np.copy(platform)
    for coord, dirs in beam_tracking.items():
        if plat[coord[0], coord[1]] == '.':
            if len(dirs)==1:
                plat[coord[0], coord[1]] = dirs[0]
            else:
                plat[coord[0], coord[1]] = len(dirs)
    return plat         

plat = energize(beam_tracking, platform)
print_p(plat)

print('res part 1 =', len(beam_tracking))

leng = []
for i in range(nr):
    leng.append(len(propagate(platform, i, 0, ">")))
    leng.append(len(propagate(platform, i, nc-1, "<")))
for j in range(nc):    
    leng.append(len(propagate(platform, 0, j, "v")))
    leng.append(len(propagate(platform, nr-1, j, "^")))

print('res part 2 =', np.max(leng))
    
