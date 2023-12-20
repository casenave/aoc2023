print("required python >=3.10\n======")

import numpy as np
import io

def run_part_1(data_string):

    input = io.StringIO(data_string).readlines()

    destinations = {}
    types = {}
    states = {}
    origins = {}
    latest_pulses = {}


    for line in input:
        l = line.split(" -> ")

        key = l[0][1:].strip()
        state = None

        match l[0][0]:
            case "b":
                key = "broadcaster"
                type = "broadcaster"
            case "%":
                type = "%"
                state = "off"
            case "&":
                type = "&"


        destinations[key] = [a.strip() for a in l[1].split(", ")]
        types[key] = type
        states[key] = state
        latest_pulses[key] = "low"
        origins[key] = []


    for key, dest in destinations.items():
        if type == "&":
            for d in dest:
                origins.setdefault(d, []).append(key)


    def update(pulse_intensity, dest):
        lp = pulse_intensity
        new_pulses = []
        count_high = 0
        count_low = 0
        for d in dest:
            if pulse_intensity == "high":
                count_high += 1
            else:
                count_low += 1
            new_pulses.append([d, pulse_intensity])
        # print("input =", location, pulse_intensity)
        # print("output =", new_pulses, latest_pulses, count_high, count_low)
        # print("====")
        return new_pulses, lp, count_high, count_low

    def treat_pulses(lp, energy, type, state, latest_pulses, dest, origs):

        # print("location, energy =", location, energy)
        # print("state, destinations =", states[location], destinations[location])

        new_pulses = []
        count_high = 0
        count_low = 0

        match type:
            case "broadcaster":
                assert energy == "low"
                new_pulses = [[d, "low"] for d in dest]
                for _ in dest:
                    count_low += 1
            case "%":
                match energy:
                    case "high":
                        # pulses, latest_pulses, string = update(pulses, latest_pulses, string, destinations, location, "high")
                        # for d in destinations[location]:
                        #     string += location+" -high-> "+d+"\n"
                        True
                    case "low":
                        match state:
                            case "on":
                                state = "off"
                                new_pulses, lp, count_high, count_low = update("low", dest)
                                # for d in destinations[location]:
                                #     pulses.append([d, "low"])
                                #     latest_pulses[d] = "low"
                                #     string += location+" -low-> "+d+"\n"
                            case "off":
                                state = "on"
                                new_pulses, lp, count_high, count_low = update("high", dest)
                                # for d in destinations[location]:
                                #     pulses.append([d, "high"])
                                #     latest_pulses[d] = "high"
                                #     string += location+" -high-> "+d+"\n"
                        # print("%, location, states[location] =", location, states[location])

            case "&":
                # condition = np.all([True for a in origins[location] if latest_pulses[a] == "high"])
                # print(">>", origins[location], [latest_pulses[a] for a in origins[location]])
                # print(condition, location, destinations[location])
                # print("latest_pulses of origins", location, origins[location], "=", [latest_pulses[a] for a in origins[location]])
                # print("WW", np.all([latest_pulses[a] for a in origins[location]]==len(origins[location])*["high"]))
                if np.all([latest_pulses[a] for a in origs]==len(origs)*["high"]):
                    new_pulses, lp, count_high, count_low = update("low", dest)
                else:
                    new_pulses, lp, count_high, count_low = update("high", dest)
                # print(pulses)


        # pulses = pulses[1:]
        # print(">>", pulses, states[location])
        # print(string)
        # print("===")
        # pulses = pulses[len(destinations[location]):]
        # print(len(pulses))
        return new_pulses, state, lp, latest_pulses, count_high, count_low




    nb_pushes = 1000


    total_count_high = 0
    total_count_low = 0
    # for _ in tqdm(range(nb_pushes)):
    for _ in range(nb_pushes):

        pulses = [["broadcaster", "low"]]
        total_count_low += 1
        string = "button -low-> broadcaster\n"

        count = 0



        while len(pulses) > 0:

            # print("test =", len(pulses), len([p for p in pulses if p[0] == 'rx']) == len(pulses), pulses, [p for p in pulses if p[0] == 'rx'])

            location = pulses[0][0]
            energy = pulses[0][1]

            if location in types:
                
                type = types[location]
                state = states[location]

                origs = origins[location]
                dest = destinations[location]
                lp = latest_pulses[location]

                new_pulses, state, lp, latest_pulses, count_high, count_low = treat_pulses(lp, energy, type, state, latest_pulses, dest, origs)

                states[location] = state
                latest_pulses[location] = lp

                pulses += new_pulses

                total_count_high += count_high
                total_count_low += count_low

            pulses.pop(0)


        # total_count_high += local_count_high
        # total_count_low += local_count_low

        # count_high += pulses_count["high"]
        # count_low += pulses_count["low"]
        # print(pulses)
        # print(string)
        # # out_pulses = treat_pulses(out_pulses[0])
        # # print(out_pulses)

        # print("flip-flop state =", [(k,v) for k, v in states.items() if types[k]=="%"])
        # print("====")
        # print("pulses_count =", pulses_count)

    return total_count_high*total_count_low


EXAMPLE_1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

EXAMPLE_2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

print('assert part 1 example 1 correct ?', run_part_1(EXAMPLE_1)==32000000)
print('assert part 1 example 2 correct ?', run_part_1(EXAMPLE_2)==11687500)


    
