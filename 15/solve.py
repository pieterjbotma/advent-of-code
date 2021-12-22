from functools import cache
from time import time_ns
import sys
import gc
from collections import defaultdict
from bisect import bisect

H = 3
sys.setrecursionlimit(int(1e4))

grid = tuple(tuple(map(int,line.strip())) for line in open('example.txt'))
Y = len(grid)
X = len(grid[0])

@cache
def expand(point):
    return [[(point+x+y-1)%9+1 for x in range(5)] for y in range(5)]


grid = [[expand(grid[y%Y][x%X])[int(y/Y)][int(x/X)] for x in range(5*X)] for y in range(5*Y)]
Y = len(grid)
X = len(grid[0])

totals = [(X+Y)*H]
paths_dict = defaultdict(list,{totals[0]:[(0,0,0)]})

found = 0
found_totals = set()
while found < 1:
    min_total = totals.pop(0)
    paths = paths_dict.pop(min_total)
    for x,y,risk in paths:
        if y==Y-1 and x==X-1:
            found+=1
            found_totals.add(risk)
            continue
        if (newX:= x+1) < X:
            new_total = min_total+grid[newX][y]-H
            paths_dict[new_total].append((newX,y,risk+grid[newX][y]))
            if not totals:
                totals.append(new_total)
            elif totals[(idx:=bisect(totals,new_total))-1] != new_total:
                totals.insert(idx,new_total)
        if (newY:= y+1) < Y:
            new_total = min_total+grid[x][newY]-H
            paths_dict[new_total].append((x,newY,risk+grid[x][newY]))
            if not totals:
                totals.append(new_total)
            elif totals[(idx:=bisect(totals,new_total))-1] != new_total:
                totals.insert(idx,new_total)

# print(found_totals)
# print(min(found_totals))

###################

Y = len(grid)
X = len(grid[0])
min_total = 400

@cache
def step(y,x,total):
    global min_total
    total += grid[y][x]
    if total+H*(Y-1-y)+H*(X-1-x) >= min_total:
        pass
    elif y==Y-1 and x==X-1:
        min_total = total
    else:
        if y < Y-1:
            step(y+1,x,total)
        if x < X-1:
            step(y,x+1,total)

start = time_ns()
step(0,0,-grid[0][0])
print((time_ns()-start)*1e-9)
print(min_total)
