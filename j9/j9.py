

with open('j9_input.txt') as f:
    input = f.readlines()


from copy import copy
def treat_sequence(sequence):
    seq = [copy(sequence)]
    count = 0
    while seq[count].count(0) != len(seq[count]):
        seq.append([seq[count][i+1]-seq[count][i] for i in range(len(seq[count])-1)])
        count += 1
    seq[count].append(0)
    for i in range(len(seq)-2, -1, -1):
        seq[i].append(seq[i+1][-1]+seq[i][-1])
    return seq[0][-1]


res = 0
for line in input:
    sequence = [int(n) for n in line.strip().split(" ")]
    res += treat_sequence(sequence)

print('res part 1 =', res)



def treat_sequence_2(sequence):
    seq = [copy(sequence)]
    count = 0
    while seq[count].count(0) != len(seq[count]):
        seq.append([seq[count][i+1]-seq[count][i] for i in range(len(seq[count])-1)])
        count += 1
    seq[count].insert(0, 0)
    for i in range(len(seq)-2, -1, -1):
        seq[i].insert(0, seq[i][0]-seq[i+1][0])
    return seq[0][0]

res = 0
for line in input:
    sequence = [int(n) for n in line.strip().split(" ")]
    res += treat_sequence_2(sequence)

print('res part 2 =', res)
    
