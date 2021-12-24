from math import prod
from operator import gt,lt,eq
from typing import List

with open('example.txt') as f:
    input = f.read()
m = bin(int(input,16))[2:].zfill(len(input)*4)

versions = []

list_operators = {0:sum, 1:prod, 2:min, 3:max}
pair_operators = {5:gt, 6:lt, 7:eq}

def dec(message,packets:List):
    v,t,i,l0,l1 = tuple(int(message[slice(start, stop)],2) for start, stop in [(0,3),(3,6),(6,7),(7,22),(7,18)])
    versions.append(v)
    if t==4:
        literal = ""
        o = 6
        while int(message[o]):
            literal+=message[o+1:o+5]
            o+=5
        literal+=message[o+1:o+5]
        o+=5
        packets.append(int(literal,2))
    else:
        sub_packets = []
        if i==0:
            o=22
            while o < 22+l0:
                o+=dec(message[o:],sub_packets)
        else:
            o=18
            for _ in range(l1):
                o+=dec(message[o:],sub_packets)
        if t in list_operators:
            packets.append(list_operators[t](sub_packets))
        if t in pair_operators:
            packets.append(int(pair_operators[t](*sub_packets)))
    return o

packets = []
dec(m,packets)
print(sum(versions))
print(packets)