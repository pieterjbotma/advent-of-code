from functools import cache
from time import time_ns
import sys
import gc
from collections import defaultdict
from bisect import bisect
import heapq

H = 3
sys.setrecursionlimit(int(1e4))

grid = tuple(tuple(map(int,line.strip())) for line in open('example.txt'))
Y = len(grid)
X = len(grid[0])

@cache
def expand(point):
    return [[(point+x+y-1)%9+1 for x in range(5)] for y in range(5)]

# grid = [[expand(grid[y%Y][x%X])[int(y/Y)][int(x/X)] for x in range(5*X)] for y in range(5*Y)]
# Y = len(grid)
# X = len(grid[0])

min_risk = [[0 for x in range(X)] for y in range(Y)] 

x=0
y=0

def neighbours(x,y):
    return ((nx,ny) for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)] if 0 <= (nx:=x+dx) < X and 0 <= (ny:=y+dy) < Y)

print(neighbours)

for gridline in min_risk:
    print(gridline)

paths = [(0,(0,0))]

while paths:
    

for neighbour in neighbours():

heapq.heappush(neighbour for neighbour in neighbours)
