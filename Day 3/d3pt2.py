from collections import Counter

filename = "C:\\Users\\wcorr\\Desktop\\AoC 2021\\Day 3\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [list(x.strip()) for x in content]

# Disgusting recursion
def recur(indx, lsts, o2orco2):
    counter_index = 0 if o2orco2 == "o2" else -1
    lsts_count = [Counter(z) for z in zip(*lsts)]

    are_equally_common = lsts_count[indx].most_common()[counter_index][1] == len(lsts)/2
    value_if_equal = 1 if o2orco2 == "o2" else 0

    if len(lsts) == 1 or indx == len(content[0]):
        return lsts
    else:
        most_common_value = lsts_count[indx].most_common()[counter_index][0]
        return recur(indx + 1, list(filter(lambda x : parse_x_value(x[indx], are_equally_common, value_if_equal, most_common_value), lsts)), o2orco2)

# Disgusting recursion filter
def parse_x_value(value_of_x, are_equally_common, value_if_equal, most_common_value):
    if are_equally_common:
        return int(value_of_x) == int(value_if_equal)
    else:
        return int(value_of_x) == int(most_common_value)

oxygen_generator_rating = "".join(recur(0, content, "o2")[0])
co2_scrubber_rating = "".join(recur(0, content, "co2")[0])
life_support_rating = int(oxygen_generator_rating, base=2) * int(co2_scrubber_rating, base=2)

# Correct answers only please
print(oxygen_generator_rating)
print(co2_scrubber_rating)

print(life_support_rating)

