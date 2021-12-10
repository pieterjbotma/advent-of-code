from functools import lru_cache, reduce
from time import time_ns

initial_fish = list(map(int,open('day6-input.txt').read().split(',')))

DAYS = 256

@lru_cache
def add_fish(day, age):
    return reduce(lambda count, day: count+add_fish(day, 8), range(day+age+1, DAYS+1, 7), 1)

start = time_ns()
print(sum(add_fish(0,fish) for fish in initial_fish))
print((time_ns()-start)/1e6)

start = time_ns()
age_list = [initial_fish.count(i) for i in range(9)]
for _ in range(256):
    fish=age_list.pop(0)
    age_list.append(fish)
    age_list[6]+=fish

print(sum(age_list))
print((time_ns()-start)/1e6)







# for _ in range(18):
#     new_fish = [8 for age in fish if age==0]
#     fish = [6 if age==0 else age-1 for age in fish]
#     fish.extend(new_fish)

# print(len(fish))
