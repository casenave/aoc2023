print("DISCLAMER: solution taken from https://topaz.github.io/paste/#XQAAAQAxBQAAAAAAAAAzHIoib6pXbueH4X9F244lVRDcOZab5q1+VXY/ex42qR7D+RJIst2kujM5bGuOD3oaz/6Pv64SYp4BPkcF/7KxTVGvEJxxwMxAiDKNcmos1j8t62RwbNmhOw50Lq9qCl/Ga8E3QuTvNLkvRXgvq4gJ/3OOvXyu2XUYN4NFeYos8GftDMIYYSnC6jQ2yeK+iULXzTyl/98ite7K0+0qlsfOSYGKKNK5TQzTWynCD+ViwaokYOFxiX9zkvELdBRKcTsoIpqAOqGjl+6dbYJSrH/6GZ6rLVMY8t5pK2hRE26v7rNOhHWCThxAQ0ztvtPvxdfkryB3SVMq+bbnkpYBGwwWpdERRrOJVcmATNEmr889YkLtlFvVPMqTzZKuvfKPQsU2dbWNfLQssvRDJ51/mxkCRuTs1dtB0MLJ+z6xTtLljBBCI6tJmjT1BrB04xiRcWm80SdH8EivMpIKuzYsP6evqv7SwD8meqJDdBue93hioPdm281oxHT8LrL7eJdFIcQS/TrYiXoLU7T6OCt51s5SOR/KcxFXoEUdQ2AK2k2bqcSl9tsK90At8h8pOA+rGNwSbZVfDrrgqlun/MaRi5vppGw8SvndPRo15aoGPpVpyIdmjidhLLKXo87PlvOCoW7hN8WLV2+qVc8O3pt0S5tzydtYI0r8WN6IC5xA/xdMPwVyzO7UlzaBcx5/9fDFi2t7NyekR1ND3hD9QcVy9aD5bFBjHdzqcphonCUjR1pqgzK4STOEFVAoH30R7Dw/dBzHppuZczrUXn+grJR4YMcK4A22tuTdPeu0X/8wHFIA\n=========")

from collections import defaultdict
from math import prod


modules = dict()
flips = defaultdict(int)
conjs = defaultdict(dict)

for line in open('j20_input.txt'):
    s, _, *ds = line.replace(',', '').split()
    t, s = (s[0], s[1:]) if s[0] in '%&' else ('', s)

    modules[s] = t, ds

    for d in ds:
        conjs[d][s] = 0
        if d == 'rx': rx = s

rx_ins = {i: 0 for i in conjs[rx]}

presses = 0
counts = [0, 0]

while True:
    if presses == 1000:
        print('res part 1 =', prod(counts))
    presses += 1

    if all(rx_ins.values()):
        print('res part 2 =', prod(rx_ins.values()))
        break

    queue = [(None, 'broadcaster', 0)]
    while queue:
        source, mod, pulse_in = queue.pop(0)
        counts[pulse_in] += 1

        if mod not in modules: continue
        type, nexts = modules[mod]

        match type, pulse_in:
            case '', _:
                pulse_out = pulse_in
            case '%', 0:
                pulse_out = flips[mod] = not flips[mod]
            case '&', _:
                conjs[mod][source] = pulse_in
                pulse_out = not all(conjs[mod].values())

                if 'rx' in nexts:
                    for k, v in conjs[mod].items():
                        if v: rx_ins[k] = presses
            case _,_: continue

        for n in nexts:
            queue.append((mod, n, pulse_out))