v = (7,0)
p = (0,0)
# target = ((20,30),(-10,-5))
target = ((207,263),(-115,-63))

def step(p,v):
    np = (p[0]+v[0], p[1]+v[1])
    nv = (v[0]-1 if v[0]>0 else v[0]+1 if v[0]<0 else v[0], v[1]-1)
    return np,nv

print(p,v)
x_velocities = []
y_velocities = []

v0 = 0
while p[0] <= target[0][1]:
    v0+=1
    v = (v0,0)
    p = (0,0)
    while v[0] > 0:
        p,v = step(p,v)
    if target[0][0] <= p[0] <= target[0][1]:
        x_velocities.append(v0)

for v0 in x_velocities:
    for v1 in range(1000):
        v = (v0,v1)
        p = (0,0)
        while p[1] >= target[1][0]:
            p,v = step(p,v)
            if target[1][0] <= p[1] <= target[1][1]:
                y_velocities.append(v1-1)

print(max(y_velocities))
print(sum(range(max(y_velocities)+1)))
print(sum(range(115)))
