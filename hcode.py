#!/usr/bin/env pypy
import sys
import math


def fdistance(l1, l2):
    return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])

"""if len(sys.argv) < 3:
    print("Not enough params")
    exit(1)"""

fname = "a_example.in"
if len(sys.argv) > 1:
    fname = sys.argv[1]

rideData = {}

with open(fname, 'r') as f:
    # 3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
    rows, columns, nvehicles, rides, bonus, steps = [int(x) for x in f.readline()[0:-1].split(" ")]
    vehicles = []
    for i in range(nvehicles):
        vehicles.append([[0,0], 0, []])
    lines = f.readlines()
    for index, line in enumerate(lines):
        vals = [int(x) for x in line[0:-1].split(" ")]
        start = vals[0:2]
        end = vals[2:4]
        earlyStart = int(vals[4])
        earlyEnd = int(vals[5])
        distance = fdistance(start, end)
        rideData[index] = [index, start, end, earlyStart, earlyEnd, distance]

for step in range(steps):
    if len(rideData) == 0:
        break
    for v in vehicles:
        smallestDist = 999999999
        nearestI = -1
        for k, ride in rideData.items():
            distance = fdistance(v[0], ride[1])
            if distance < smallestDist:
                smallestDist = distance
                nearestI = ride[0]
        if nearestI != -1:
            a = rideData[nearestI]
            v[1] = a[5]
            v[2].append(a[0])
            v[0] = a[2]
            del rideData[nearestI]

for v in vehicles:
    sys.stdout.write(str(len(v[2])) + " ")
    for e in v[2]:
        sys.stdout.write(str(e) + " ")
    sys.stdout.write('\n')