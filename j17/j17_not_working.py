import numpy as np
import heapq

with open('j17_input.txt') as f:
    input = f.readlines()

map = []
for line in input:
    map.append([int(l) for l in line.strip()])

map = np.array(map, dtype=int)
nr = map.shape[0]
nc = map.shape[1]


# convert map to graph
graph = {}
for i in range(nr):
    for j in range(nc):
        graph[(i,j)] = []
        if 0<=i-1:
            graph[(i,j)].append(((i-1,j),map[i-1,j]))
        if i+1<nr:
            graph[(i,j)].append(((i+1,j),map[i+1,j]))
        if 0<=j-1:
            graph[(i,j)].append(((i,j-1),map[i,j-1]))
        if j+1<nc:
            graph[(i,j)].append(((i,j+1),map[i,j+1]))

def dir(u,v):
    delta = np.array(v)-np.array(u)
    if np.all(delta==[0,1]):
        return ">"
    if np.all(delta==[0,-1]):
        return "<"
    if np.all(delta==[1,0]):
        return "v"
    if np.all(delta==[-1,0]):
        return "^"
    

opposites = {'^':'v', 'v':'^', '<':'>', '>':'<', 'o':''}

def straight_condition(u, v, dirs, min_straight, max_straight):
    i = len(dirs)-1
    dir_ = dir(u,v)
    if opposites[dirs[-1]] == dir_:
        return False
    last_identical_dirs = 0
    while dirs[i] == dirs[-1] and i>=0:
        i-=1
        last_identical_dirs += 1
    condition_max = False
    if last_identical_dirs<max_straight or dirs[-1]!=dir_:
        condition_max = True
    condition_min = False
    if last_identical_dirs>=min(len(dirs)-1,min_straight):
        condition_min = True

    return condition_max and condition_min


from copy import copy

def modified_lazy_dijkstras(graph, root, min_straight, max_straight):
    # set up "inf" distances
    dist = {}
    for i in range(nr):
        for j in range(nc):
            dist[(i,j)] = np.inf
    dist[root] = 0
    path = {}
    for i in range(nr):
        for j in range(nc):
            path[(i,j)] = []
    path[root] = [root]
    dirs = {}
    for i in range(nr):
        for j in range(nc):
            dirs[(i,j)] = []
    dirs[root] = ['o']

    visited = {}
    for i in range(nr):
        for j in range(nc):
            visited[(i,j)] = False

    pq = [(0, root)]
    while len(pq) > 0:

        _, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v, l in graph[u]:
            sc2 = straight_condition(u, v, dirs[u], min_straight, max_straight)
            if dist[u] + l < dist[v] and sc2:
                dist[v] = dist[u] + l
                dirs[v] = copy(dirs[u])
                dirs[v].append(dir(u,v))
                path[v] = copy(path[u])
                path[v].append(v)
                heapq.heappush(pq, (dist[v], v))

    return dist, path, dirs

def plot_tentative(map, path, dirs):
    map_ = np.empty(map.shape, dtype=str)
    for i in range(map_.shape[0]):
        for j in range(map_.shape[1]):
            map_[i,j] = '.'
    for I in range(len(path)):
        map_[path[I][0], path[I][1]] = dirs[I]
    string_ = ""
    for i in range(map_.shape[0]):
        string_ += "".join(map_[i,:])+"\n"
    string_ = string_[:-1]
    print(string_)


dist, path, dirs = modified_lazy_dijkstras(graph, (0,0), 0, 3)

plot_tentative(map, path[(nr-1,nc-1)], dirs[(nr-1,nc-1)])

print("res part 1 =", dist[(nr-1,nc-1)])

dist, path, dirs = modified_lazy_dijkstras(graph, (0,0), 3, 10)
print("res part 2 =", dist[(nr-1,nc-1)])