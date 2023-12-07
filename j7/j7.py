import numpy as np

with open('j7_input.txt') as f:
    input = f.readlines()


labels_ranks = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6,
                 "6":5, "5":4, "4":3, "3":2, "2":1}


hands = []
bids  = []

for line in input:
    l = line.split(" ")
    hands.append(l[0].strip())
    bids.append(int(l[1].strip()))


def compute_types(hand):
    assert len(hand)==5
    hand = [h for h in hand]
    set_ = list(set(hand))
    nbe_unique = len(set_)
    if nbe_unique == 1:
        return 1
    elif nbe_unique == 2:
        if hand.count(set_[0]) == 4 or hand.count(set_[1]) == 4:
            return 2
        else:
            return 3
    elif nbe_unique == 3:
        if hand.count(set_[0]) == 3 or hand.count(set_[1]) == 3 or hand.count(set_[2]) == 3:
            return 4
        else:
            return 5
    elif nbe_unique == 4:
        return 6
    elif nbe_unique == 5:
        return 7
    else:
        raise


import copy
def rank_hands(alphabet, local_hands):

    ranked_local_hands = sorted(local_hands, key=lambda word: [alphabet.index(c) for c in word])
    local_ranks = np.array([ranked_local_hands.index(hand) for hand in local_hands])

    return local_ranks
        


types = np.zeros(len(hands), dtype = int)
for i, hand in enumerate(hands):
    types[i] = compute_types(hand)




alphabet = "23456789TJQKA"

ranks = -1*np.ones(len(hands), dtype = int)
count = 0
for i in range(7, 0, -1):

    local_types = types[types==i]
    local_indices = np.arange(len(hands))[types==i]
    local_hands = [hands[j] for j in local_indices]

    local_ranks = rank_hands(alphabet, local_hands)

    ranks[local_indices] = count + local_ranks
    count += len(local_types)

inv_ranks = np.argsort(ranks)
res = 0
for i in range(len(hands)):
    res += (i+1)*bids[inv_ranks[i]]



print('res part 1 =', res)


from copy import copy
def compute_types_2(alphabet, hand):
    assert len(hand)==5

    tentative_types = []
    
    if "J" in hand:
        for l in alphabet[1:]:
            iter_hand = copy(hand)
            iter_hand = iter_hand.replace("J", l)
            tentative_types.append(compute_types(iter_hand))
    else:
        tentative_types.append(compute_types(hand))

    return min(tentative_types)


alphabet = "J23456789TQKA"

types = np.zeros(len(hands), dtype = int)
for i, hand in enumerate(hands):
    types[i] = compute_types_2(alphabet, hand)


ranks = -1*np.ones(len(hands), dtype = int)
count = 0
for i in range(7, 0, -1):

    local_types = types[types==i]
    local_indices = np.arange(len(hands))[types==i]
    local_hands = [hands[j] for j in local_indices]

    local_ranks = rank_hands(alphabet, local_hands)

    ranks[local_indices] = count + local_ranks
    count += len(local_types)

inv_ranks = np.argsort(ranks)
res = 0
for i in range(len(hands)):
    res += (i+1)*bids[inv_ranks[i]]

print('res part 2 =', res)
    
