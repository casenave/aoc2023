import numpy as np

with open('j18_input.txt') as f:
    input = f.readlines()


directions = []
lengths = []
colors = []
for line in input:
    data = line.split(" ")
    directions.append(data[0])
    lengths.append(int(data[1]))
    colors.append(data[2].strip()[1:-1])



def build_polygon(directions, lengths):
    x = [0]
    y = [0]
    for i, (dir, len) in enumerate(zip(directions, lengths)):
        if dir == 'D':
            x.append(x[i]+len)
            y.append(y[i])
        elif dir == 'U':
            x.append(x[i]-len)
            y.append(y[i])
        elif dir == 'R':
            x.append(x[i])
            y.append(y[i]+len)
        elif dir == 'L':
            x.append(x[i])
            y.append(y[i]-len)

    min_x = np.min(x)
    min_y = np.min(y)
    
    x = x-min_x
    y = y-min_y

    return np.array(x), np.array(y)

x, y = build_polygon(directions, lengths)

 
i = np.arange(len(x))
shoelace = np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5)

res = int(shoelace + np.sum(lengths)//2 + 1)
print('res part 1 =', res)


directions = []
lengths = []

def convert_colors(colors):
    directions = []
    lengths = []
    for c in colors:
        lengths.append(int(c[1:-1], 16))
        if c[-1] == "0":
            directions.append("R")
        elif c[-1] == "1":
            directions.append("D")
        elif c[-1] == "2":
            directions.append("L")
        elif c[-1] == "3":
            directions.append("U")
    return directions, lengths

directions, lengths = convert_colors(colors)

x, y = build_polygon(directions, lengths)

i = np.arange(len(x))
shoelace = np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5)

res = int(shoelace + np.sum(lengths)//2 + 1)
print('res part 2 =', res)
