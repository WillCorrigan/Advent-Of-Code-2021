from collections import Counter, defaultdict
import statistics

initial_state = None

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    initial_state = [x.strip().split(",") for x in content]
    initial_state = [int(x) for lst in initial_state for x in lst]

median = statistics.median(initial_state)

answer = sum([abs(x - median) for x in initial_state])

print(answer)

