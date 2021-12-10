
crabs = list(map(int,open('day7-input.txt').read().split(',')))

def fuel_cost(dist):
    return (dist*(dist+1))>>1

fuel_costs = [sum([fuel_cost(abs(crab-pos)) for crab in crabs]) for pos in range(max(crabs))]

print(min(fuel_costs))

# median = int(np.median(crabs))
# print(sum([abs(pos-median) for pos in crabs]))


