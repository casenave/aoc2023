

with open('j8_input.txt') as f:
    input = f.readlines()


directions_ = input[0].strip()
size = len(directions_)

directions = []
for i in range(size):
    if directions_[i] == "L":
        directions.append(0)
    else:
        directions.append(1)

maps = {}
for line in input[2:]:
    current_position = line[0:3]
    left = line[7:10]
    right = line[12:15]
    maps[current_position] = (left, right)

position = 'AAA'

count = 0
while position != "ZZZ":
    position = maps[position][directions[count%size]]
    count += 1

print('res part 1 =', count)


paths = [k for k in list(maps.keys()) if k[-1] == 'A']
nb_of_paths = len(paths)


c_l = []
for position in paths:
    count = 0
    cycle_length = 0
    cycle_finder = []
    while True:
        position = maps[position][directions[count%size]]
        count += 1
        cycle_length += 1
        if position[-1] == 'Z':
            if count%size in cycle_finder:
                break
            else:
                cycle_finder.append(count%size)   
                cycle_length = 0

    c_l.append(cycle_length)


from math import gcd
lcm = 1
for i in c_l:
    lcm = lcm*i//gcd(lcm, i)

print('res part 2 =', lcm)
    
