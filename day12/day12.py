from typing import Dict, List, Set
from collections import defaultdict
from time import time_ns

caves: Dict[str,List[str]] = defaultdict(list)
for line in open('day12-input.txt'):
    a,b = line.strip().split('-')
    if a != 'end' and b != 'start':
        caves[a].append(b)
    if a != 'start' and b != 'end':
        caves[b].append(a)

small_caves = [cave for cave in caves if cave.islower() and cave not in ('start','end')]

def check_cave(path: List[str], paths: Set, single_caves, double_cave):
    if (cave:=path[-1]) == 'end':
        paths.add(tuple(path))
    elif cave in single_caves and path.count(cave) > 1:
        pass
    elif cave == double_cave and path.count(cave) > 2:
        pass
    else:
        for connection in caves[cave]:
            path.append(connection)
            check_cave(path, paths, single_caves, double_cave)
            path.pop()

start = time_ns()
paths = set()
for double_cave in small_caves:
    single_caves = tuple(cave for cave in small_caves if cave != double_cave)
    check_cave(['start'],paths,single_caves,double_cave)
print(len(paths))
print((time_ns()-start)/1e9)
