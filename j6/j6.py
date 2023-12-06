

with open('j6_input.txt') as f:
    input = f.readlines()

times = [int(t) for t in input[0][10:].split()]
distances = [int(d) for d in input[1][10:].split()]

dists = []
nbe_winning_races = []
for I, time in enumerate(times):
    dists.append([])
    for t in range(time+1):
        hold_duration = t
        travel_duration = time-t
        speed = t
        dists[I].append(speed*travel_duration)
    count = 0
    for d in dists[I]:
        if d>distances[I]:
            count += 1
    nbe_winning_races.append(count)


res = 1
for wr in nbe_winning_races:
    res *= wr


print('res part 1 =', res)


time = int(input[0][10:].strip().replace(" ", ""))
distance = int(input[1][10:].strip().replace(" ", ""))

def winning_race(tested_time, time, distance)->bool:
    travel_duration = time-tested_time
    speed = tested_time
    return speed*travel_duration > distance


low = 0
high = time
converged = False
while converged == False:
    tested_time = (high+low)//2
    if winning_race(tested_time, time, distance) == True:
        high = tested_time
    else:
        low = tested_time
    if high-low<2:
        converged = True

print('res part 2 =', time-2*high+1)
    
