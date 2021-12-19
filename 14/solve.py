from functools import cache, partial, reduce
from collections import Counter
from typing import Tuple
from operator import add

with open('input.txt') as f:
    template = f.readline().strip()
    _ = f.readline()
    rules = {tuple(pair):((pair[0],element),(element,pair[1])) for pair,element in (line.strip().split(' -> ') for line in f)}

@cache
def count_elements(steps, pairs:Tuple):
    return Counter([pair[0] for pair in pairs]) if steps==0 else reduce(add,map(partial(count_elements,steps-1),(rules[pair] for pair in pairs)))

pairs = tuple((template[i],template[i+1]) for i in range(len(template[:-1])))
counts = count_elements(40,pairs)+Counter(pairs[-1][-1])
print(counts.most_common()[0][1]-counts.most_common()[-1][1])
