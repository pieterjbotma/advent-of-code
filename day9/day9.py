from functools import reduce
from operator import mul

m = [list(map(int,line.strip())) for line in open('day9-input.txt')]

def map_to_neighbour(func,r,c,):
    if r>0:
        func(r-1,c)
    if r<len(m)-1:    
        func(r+1,c)
    if c>0:
        func(r,c-1)
    if c<len(m[0])-1:
        func(r,c+1)

def is_low(r,c):
    is_higher=[]
    map_to_neighbour(lambda R,C: is_higher.append(m[R][C] > m[r][c]), r, c)
    return all(is_higher)

def add_to_basin(basin: list,r,c):
    if m[r][c]!=9:
        basin.append(m[r][c])
        m[r][c] = 9
        map_to_neighbour(lambda R,C: add_to_basin(basin, R, C), r, c)
    return basin

low_points = list((r,c) for r in range(len(m)) for c in range(len(m[0])) if is_low(r, c))

print(sum(m[r][c]+1 for r,c in low_points))
print(reduce(mul, sorted([len(add_to_basin([],r,c)) for r,c in low_points])[-3:]))
