with open('day5_input.txt') as f:
    lines = [[tuple(map(int,coords.split(','))) for coords in line.strip().split(' -> ')] for line in f]
        
chart = [[0 for _ in range(1000)] for _ in range(1000)]

def mark_point(p,end):
    chart[p[1]][p[0]]+=1
    if p!=end:
        next_coord = tuple(p[i]+1 if p[i]<end[i] else p[i]-1 if p[i]>end[i] else p[i] for i in range(2))
        mark_point(next_coord, end)

for line in lines:
    # if all([line[0][i]!=line[1][i] for i in range(2)]):
    #     continue
    mark_point(*line)

print(sum(1 for line in chart for point in line if point >= 2))