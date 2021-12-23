from functools import cache
from time import time_ns
import heapq

grid = tuple(tuple(map(int,line.strip())) for line in open('input.txt'))
Y = len(grid)
X = len(grid[0])

@cache
def expand(point):
    return [[(point+x+y-1)%9+1 for x in range(5)] for y in range(5)]

grid = [[expand(grid[y%Y][x%X])[int(y/Y)][int(x/X)] for x in range(5*X)] for y in range(5*Y)]
Y = len(grid)
X = len(grid[0])

@cache
def neighbours(x,y):
    return ((nx,ny) for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)] if 0 <= (nx:=x+dx) < X and 0 <= (ny:=y+dy) < Y)

visited = set()
points_to_check = [(0,0,0)]

while points_to_check:
    risk,x,y = heapq.heappop(points_to_check)
    if (x,y) == (X-1,Y-1):
        print(risk)
        break
    for nx,ny in neighbours(x,y):
        if (nx,ny) not in visited:
            heapq.heappush(points_to_check,(risk+grid[ny][nx],nx,ny))
    visited.add((x,y))
