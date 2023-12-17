print("DSICLAMER: solution taken from https://github.com/AllanTaylor314/AdventOfCode/blob/main/2023/17.py")

from collections import defaultdict, deque

N,E,W,S = -1j,1,-1,1j
L,R = -1j, 1j
with open("j17_input.txt") as file:
    lines = file.read().splitlines()
COSTS = {complex(x,y):int(c) for y,line in enumerate(lines) for x,c in enumerate(line)}

def solver(lower_bound, upper_bound, costs=COSTS):
    last = max(costs,key=abs)
    cost_map = defaultdict(lambda: [1e100]*upper_bound) 
    cost_map[S,S][0] = costs[S]
    cost_map[E,E][0] = costs[E]
    todo = deque([S+S,S+E,E+E])
    pending = set(todo)
    while todo:
        coord = todo.popleft()
        pending.discard(coord)
        for src in (N,E,W,S):
            current = cost_map[coord,src]
            old = current.copy()
            current[0] = min(current[0],min(
                                        *cost_map[coord-src,src*L][lower_bound:],
                                        *cost_map[coord-src,src*R][lower_bound:]
                                            )+costs[coord])
            for i in range(1,upper_bound):
                current[i] = min(current[i],cost_map[coord-src,src][i-1]+costs[coord])
            if old != current:
                for new_coord in (coord+d for d in (src,src*L,src*R) if coord+d in costs):
                    if new_coord not in pending:
                        pending.add(new_coord)
                        todo.append(new_coord)
    return min(min(cost_map[last,d][lower_bound:]) for d in (N,E,W,S))

p1 = solver(0,3)
print("res part 1 =",p1)

p2 = solver(3,10)
print("res part 2 =",p2)