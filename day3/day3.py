from functools import reduce
import copy

with open('day3_example.txt') as f:
    bit_lists = [[int(bit)] for bit in f.readline()[:-1]]
    for line in f:
        for i, bit in enumerate(line[:-1]):
            bit_lists[i].append(int(bit))

bits_to_rate = lambda bits : reduce(lambda rate, bit: rate<<1|bit, bits, 0)

# Part 1
    
gamma_bits = [int(sum(bit_list)*2>len(bit_list)) for bit_list in bit_lists]
epsilon_bits = [int(sum(bit_list)*2<len(bit_list)) for bit_list in bit_lists]

gamma_rate = bits_to_rate(gamma_bits)
epsilon_rate = bits_to_rate(epsilon_bits)

print(gamma_rate*epsilon_rate)

# Part 2

def func(bit_lists, compare, i=0):
    keep_bit = int(compare(sum(bit_lists[i])*2, len(bit_lists[i])))
    filtered_lists = [[bit for j,bit in enumerate(old_list) if bit_lists[i][j]==keep_bit] for old_list in bit_lists]
    return [list[0] for list in filtered_lists] if len(filtered_lists[0])==1 else func(filtered_lists, compare, i+1)

o2_bit_lists = copy.deepcopy(bit_lists)
co2_bit_lists = copy.deepcopy(bit_lists)
o2 = bits_to_rate(func(o2_bit_lists,lambda x,y: x>=y))
co2 = bits_to_rate(func(o2_bit_lists,lambda x,y: x<y))
print(o2*co2)
