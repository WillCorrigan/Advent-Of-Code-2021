import statistics
import math

initial_state = None

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    initial_state = [x.strip().split(",") for x in content]
    initial_state = [int(x) for lst in initial_state for x in lst]

mean = statistics.mean(initial_state)

def gauss_formula(n):
    return int((n*(n+1))/2)

answer_rounded_down = [gauss_formula(abs(x-math.floor(mean))) for x in initial_state]
answer_rounded_up = [gauss_formula(abs(x-math.ceil(mean))) for x in initial_state]

print("Answer rounded up: " + str(sum(answer_rounded_up)))
print("Answer rounded down: " + str(sum(answer_rounded_down)))