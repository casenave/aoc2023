

with open('j15_input.txt') as f:
    input = f.readlines()

code = input[0].split(',')


def convert(istr):
    res = 0
    for c in istr:
        res += ord(c)
        res *= 17
        res = res%256
    return res

res = 0
for istr in code:
    res += convert(istr)

print('res part 1 =', res)



boxes = {}
for i in range(256):
    boxes[i] = {}

for istr in code:
    if '=' in istr:
        label = istr.split('=')[0]
        box = convert(label)
        focal = int(istr.split('=')[1])
        boxes[box][label] = focal
    elif '-' in istr:
        label = istr.split('-')[0]
        box = convert(label)
        if label in boxes[box]:
            boxes[box].pop(label)

res = 0
for i, box in boxes.items():
    for j, focal in enumerate(box.values()):
        res += (i+1)*(j+1)*focal

print('res part 2 =', res)
    
