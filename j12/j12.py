with open('j12_input.txt') as f:
    input = f.readlines()

infos = []
groups = []
for line in input:
    line = line.split(" ")
    info = [inf for inf in line[0].split(".") if inf != ''] 
    group = [int(d) for d in line[1].strip().split(",")]

    infos.append(info)
    groups.append(group)


import numpy as np
import itertools

def compute_arangements(infos, groups):

    res = 0
    for I, (info, group) in enumerate(zip(infos, groups)):

        nb_springs = np.sum(group)
        existing_springs = 0
        for inf in info:
            existing_springs += inf.count('#')
        remaining_springs = nb_springs - existing_springs
            
        combinations = []
        for inf in info:
            n_unknowns = inf.count('?')
            combinations.append(itertools.product(range(2), repeat=n_unknowns))

        combinations = itertools.product(*combinations) 

        tentative_combinations = []
        for c in combinations:
            lens = sum([sum(cc) for cc in c])
            if lens == remaining_springs: 
                tentative_info = [np.array([i for i in inf], dtype=str) for inf in info]
                for i, cc in enumerate(c):
                    cc = np.array(cc)
                    filtered_indices = np.arange(len(tentative_info[i]))[tentative_info[i]=='?']
                    tentative_info[i][filtered_indices[cc==1]] = "#"
                    tentative_info[i][filtered_indices[cc==0]] = "."
                    
                tti = ["".join(ti).split(".") for ti in tentative_info]
                tentative_info = []
                for ti in tti:
                    for t in ti:
                        if t != '':
                            tentative_info.append(t)  
                
                possible = True
                if len(tentative_info) != len(group):
                    possible = False
                for II in range(min(len(group), len(tentative_info))):
                    if len(tentative_info[II]) != group[II]:
                        possible = False

                if possible == True:            
                    tentative_combinations.append(tentative_info)   


        res += len(tentative_combinations)

    return res

print('res part 1 =', compute_arangements(infos, groups))

    
