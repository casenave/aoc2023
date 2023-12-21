import numpy as np
import io
from functools import cache


def plot_m(map):
    string =""
    for i in range(map.shape[0]):
        string += "".join(map[i])+"\n"
    print(string[:-1])


def plot_p(map, pos):
    map_ = np.copy(map)
    for p in pos:
        map_[p[0], p[1]] = "O"
    plot_m(map_)


def run_part_1(nb_steps, data_string = None):

    if data_string == None:
        with open('j21_input.txt') as f:
            input = f.readlines()
    else:
        input = io.StringIO(data_string).readlines()

    map = []
    for i, l in enumerate(input):
        line = [a for a in l.strip()]
        if "S" in line:
            start = (i, line.index("S"))
        map.append(line)

    map = np.array(map) 

    possible_move = ((0,1), (0,-1), (1,0), (-1,0))

    def take_a_step(cur_pos):
        new_pos = []
        for pos in cur_pos:
            for pm in possible_move:
                tentative_pos = (pos[0]+pm[0], pos[1]+pm[1])
                if map[tentative_pos] in ".S" and tentative_pos not in new_pos:
                    new_pos.append(tentative_pos)
        return new_pos

    new_pos = [start]
    for _ in range(nb_steps):
        new_pos = take_a_step(new_pos)

    # plot_p(map, new_pos)

    return len(new_pos)


EXAMPLE_PART_1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

print('assert part 1 example 1 correct ?', run_part_1(6, EXAMPLE_PART_1)==16)
print('res part 1 =', run_part_1(64))



def run_part_2(nb_steps, data_string = None):

    if data_string == None:
        with open('j21_input.txt') as f:
            input = f.readlines()
    else:
        input = io.StringIO(data_string).readlines()

    map = []
    for i, l in enumerate(input):
        line = [a for a in l.strip()]
        if "S" in line:
            start = (i, line.index("S"))
        map.append(line)

    map = np.array(map) 

    nr = map.shape[0]
    nc = map.shape[1]

    possible_move = ((0,1), (0,-1), (1,0), (-1,0))

    
    @cache
    def decide(p0, p1, pm0, pm1):
        if map[(p0+pm0)%nr, (p1+pm1)%nc] in ".S":
            return True
        else:
            return False

    new_pos = [start]
    for i in range(nb_steps):

        cur_pos = np.copy(new_pos)

        new_pos = []
        for pos in cur_pos:
            for pm in possible_move:
                d = decide(pos[0], pos[1], pm[0], pm[1])
                if d:
                    new_pos.append((pos[0]+pm[0], pos[1]+pm[1]))
        new_pos = list(set(new_pos))

    return len(new_pos)


print('assert part 2 example 1 (6 steps) correct ?', run_part_2(6, EXAMPLE_PART_1)==16)
print('assert part 2 example 1 (10 steps) correct ?', run_part_2(10, EXAMPLE_PART_1)==50)
print('assert part 2 example 1 (50 steps) correct ?', run_part_2(50, EXAMPLE_PART_1)==1594)
print('assert part 2 example 1 (100 steps) correct ?', run_part_2(100, EXAMPLE_PART_1)==6536)
# print('assert part 2 example 1 (500 steps) correct ?', run_part_2(500, EXAMPLE_PART_1)==167004)
# print('assert part 2 example 1 (1000 steps) correct ?', run_part_2(1000, EXAMPLE_PART_1)==668697)
# print('assert part 2 example 1 (5000 steps) correct ?', run_part_2(5000, EXAMPLE_PART_1)==16733044)