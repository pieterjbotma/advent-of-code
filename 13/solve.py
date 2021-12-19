from itertools import takewhile

with open('input.txt') as f:
    points = [tuple(map(int,line.split(','))) for line in takewhile(lambda line: line.strip(), f)]
    folds = [(int((fold:=line.strip().split('='))[-1]), 0 if fold[0][-1] == 'x' else 1) for line in f]

for foldline,axis in folds:
    for i, point in enumerate(points):       
        new_point = list(point)
        new_point[axis] = old if (old:=point[axis]) < foldline else foldline*2-old
        points[i] = tuple(new_point)
    points = list(set(points))
    print(len(points))

gridsize = [min(foldline for foldline,axis in folds if axis==coord) for coord in range(2)]
grid = [['#' if (x,y) in points else ' ' for x in range(gridsize[0])] for y in range(gridsize[1])]
for gridline in grid:
    print("".join(gridline))
