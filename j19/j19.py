import numpy as np

with open('j19_input.txt') as f:
    input = f.readlines()

worflows = {}
ratings = []

reading_workflows = True
for line in input:
    if line == "\n":
        reading_workflows = False
    if reading_workflows:
        l1 = line.split("{")
        l2 = l1[1].split(",")
        l2[-1] = l2[-1].strip()[:-1]
        l3 = []
        for a in l2:
            sa = a.split(":")
            if len(sa)>1:
                l3.append((sa[0], sa[1]))
            else:
                l3.append(sa)
        worflows[l1[0]] = l3
    elif len(line)>1:
        l = [a[2:] for a in line[1:-1].split(",")]
        l[-1] = l[-1].split("}")[0]
        l = [int(a) for a in l]
        ratings.append(l)


def apply_condition(rating, workflow):
    for condition in workflow:
        if len(condition) == 1:
            return condition[0]
        elif len(condition) == 2:
            x, m, a, s = rating
            if eval(condition[0]):
                return condition[1]
        else:
            raise("bad condition formatting")


accepted = []
for rating in ratings:
    active_workflow_key = 'in'
    while active_workflow_key not in 'AR':
        active_workflow_key = apply_condition(rating, worflows[active_workflow_key])

    accepted.append(active_workflow_key)


accepted = np.array(accepted)
accepted_indices = np.arange(len(accepted))[accepted=='A']



print('res part 1 =', np.sum([ratings[i] for i in accepted_indices]))


xmas = {'x':0, 'm':1, 'a':2, 's':3}

def split_interval(intervals, worflows):
    
    new_intervals = []

    for interval in intervals:
        w_key = interval[0]

        if w_key in 'AR':
            new_intervals.append((w_key, 0, interval[2]))
            continue

        w_pos = interval[1]    
        condition = worflows[w_key][w_pos]

        if len(condition)==1:
            new_intervals.append((condition[0], 0, interval[2]))
            continue

        else:
            letter = condition[0][0]
            comparison = condition[0][1]
            split_val = int(condition[0][2:])
            
            destination = condition[1]

            bounds_1 = []
            bounds_2 = []

            for i in range(4):
                if i != xmas[letter]:
                    bounds_1.append((interval[2][i][0], interval[2][i][1]))
                    bounds_2.append((interval[2][i][0], interval[2][i][1]))
                else:
                    if comparison == '>':
                        bounds_1.append((interval[2][i][0], split_val))
                        bounds_2.append((split_val+1, interval[2][i][1]))
                    else:
                        bounds_2.append((interval[2][i][0], split_val-1))
                        bounds_1.append((split_val, interval[2][i][1]))
                        
            new_intervals.append((destination, 0, tuple(bounds_2)))
            new_intervals.append((w_key, w_pos+1, tuple(bounds_1)))

    return new_intervals


intervals = [('in', 0, ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))]

while np.all([inter[0] in 'AR' for inter in intervals])==False:
    intervals = split_interval(intervals, worflows)

res = 0
for inter in intervals:
    if inter[0] == 'A':
        mult = 1
        for j in range(4):
            mult *= inter[2][j][1]-inter[2][j][0]+1
        res += mult
print('res part 2 =', res)

