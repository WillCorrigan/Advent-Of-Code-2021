from collections import Counter, defaultdict

initial_state = None

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    initial_state = [x.strip() for x in content]
    initial_state = initial_state[0].split(",")
    initial_state = [int(x) for x in initial_state]

fish_counter = Counter(initial_state)

fish_totals = defaultdict(int)

for k, v in fish_counter.items():
    fish_totals[k] = v

for day in range(1, 257):
    daily_change_dict = defaultdict(int)
    for fish_cycle, count in fish_totals.items():
        if fish_cycle == 0:
            daily_change_dict[6] += count
            daily_change_dict[8] += count
        else:
            daily_change_dict[fish_cycle-1] += count
    fish_totals = daily_change_dict

print(sum(fish_totals.values()))
                