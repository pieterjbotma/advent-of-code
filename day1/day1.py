#!/usr/bin/python

measurements = []

def rolling_sum(measurements):
    summed_measurements = []
    for i in range(len(measurements)-2):
        summed_measurements.append(sum(measurements[i:i+3]))
    return summed_measurements

def count_increases(measurements):
    increases = 0
    val = measurements[0]
    for new_val in measurements[1:]:
        increases += 1 if new_val > val else 0
        val = new_val
    return increases

with open('day1_input.txt') as f:
    for line in f:
        measurements.append(int(line))

summed_measurements = rolling_sum(measurements)

print(count_increases(summed_measurements))