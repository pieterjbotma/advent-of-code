
depth = 0
horizontal = 0
aim = 0

with open('day2_input.txt') as f:
    input = [(cmd,int(unit)) for cmd, unit in (line.split() for line in f)]
horizontal = sum(i[1] if i[0]=='forward' else 0 for i in input)
aim = [aim:=aim+i[1] if i[0]=='down' else aim-i[1] if i[0]=='up' else aim for i in input]
depth = sum(a*i[1] if i[0]=='forward' else 0 for a,i in zip(aim,input))

print(depth)
print(horizontal)

aim = depth = horizontal = 0

with open('day2_input.txt') as f:
    for line in f:
        cmd, units = line.split()
        if cmd == 'up':
            aim-= int(units)
        elif cmd == 'down':
            aim+= int(units)
        else:
            horizontal+= int(units)
            depth+= aim*int(units)

print(depth)
print(horizontal)

print(depth*horizontal)
