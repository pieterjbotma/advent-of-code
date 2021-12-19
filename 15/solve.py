from functools import cache
from time import time_ns

grid = tuple(tuple(map(int,line.strip())) for line in open('input.txt'))


# for gridline in grid:
#     print(gridline)

min_total = 9*(len(grid)+len(grid[0]))
Y = len(grid)-1
X = len(grid[0])-1

@cache
def step(y,x,total):
    global min_total
    total += grid[y][x]
    if total+(Y-y)+(X-x) >= min_total:
        pass
    elif total >= min_total:
        pass
    elif y==Y and x==X:
        min_total = total
    else:
        if y < Y:
            step(y+1,x,total)
        if x < X:
            step(y,x+1,total)

start = time_ns()
step(0,0,-grid[0][0])
print((time_ns()-start)*1e-9)
print(X,Y)
print(min_total)
