octopi = [list(map(int,line.strip())) for line in open('day11-input.txt')]
flashes = []

def age(r,c):
    octopi[r][c]+=1

def flash(r,c):
    global flashes
    if octopi[r][c] >= 10:
        flashes[-1]+=1
        octopi[r][c] = 0
        for i, row_valid in [(-1,r>0), (0,True), (1,r<len(octopi)-1)]:
            for j, col_valid in [(-1,c>0), (0,True), (1,c<len(octopi[0])-1)]:
                if row_valid and col_valid and not (i==0 and j==0):
                    octopi[(R:=r+i)][(C:=c+j)]+=int(0 < octopi[R][C])
                    flash(R,C)

while any(octopus for line in octopi for octopus in line):
    flashes.append(0)    
    for func in [age,flash]:
        for r in range(len(octopi)):
            for c in range(len(octopi)):
                func(r,c)

print(sum(flashes))
print(len(flashes))


