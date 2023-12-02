with open("j2_input.txt") as f:
    input = f.readlines()

template_bag={"red":12, "green":13, "blue":14}

sum = 0
for i, game in enumerate(input):
    game_id = i+1
    sets = game.split(":")[1].split(";")
    possible = True
    for set_ in sets:
        hands = set_.split(",")
        for hand in hands:
            hand = hand.strip().split()
            number = int(hand[0])
            color = hand[1]
            if number > template_bag[color]:
                possible = False
    if possible == True:
        sum += game_id

print("res part 1 =", sum)

sum = 0
for i, game in enumerate(input):
    sets = game.split(":")[1].split(";")
    mininum_cube_number={}
    for set_ in sets:
        hands = set_.split(",")
        for hand in hands:
            hand = hand.strip().split()
            number = int(hand[0])
            color = hand[1]
            if color in mininum_cube_number:
                if number > mininum_cube_number[color]:
                    mininum_cube_number[color] = number
            else:
                mininum_cube_number[color] = number
    power = 1
    for num in mininum_cube_number.values():
        power *= num
    sum += power

print("res part 2 =", sum)
