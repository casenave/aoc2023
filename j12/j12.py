print("DISCLAMER: memoization trick inspired from https://www.reddit.com/r/adventofcode/comments/18ge41g/2023_day_12_solutions/")

with open('j12_input.txt') as f:
    input = f.readlines()

groups = []
infos = []
for line in input:
    line = line.split(" ")
    infos.append(line[0])
    groups.append(tuple([int(d) for d in line[1].strip().split(",")]))


from functools import cache

@cache
def count_arangements(infos, groups, cur_local_len = 0):
    if not infos:
        if ((len(groups)==1 and groups[0] == cur_local_len) or (len(groups)==0 and cur_local_len == 0)):
            return 1
        return 0
    info = infos[0]
    infos = infos[1:]

    group, *new_groups = groups or [0]
    new_groups = tuple(new_groups)

    if info == '?':
        return count_arangements('#'+infos, groups, cur_local_len) + count_arangements('.'+infos, groups, cur_local_len)
    if info == '#':
        if cur_local_len > group:
            return 0
        else:
            return count_arangements(infos, groups, cur_local_len + 1)
    if info == '.':
        if cur_local_len == 0:
            return count_arangements(infos, groups, 0)
        if cur_local_len == group:
            return count_arangements(infos, new_groups, 0)
        return 0


res = 0
for info, group in zip(infos, groups):
    res += count_arangements(info, group)

print("res part 1 =", res)


res = 0
for info, group in zip(infos, groups):
    res += count_arangements("?".join(5*[info]), 5*group)

print("res part 2 =", res)