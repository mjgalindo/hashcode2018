#!/usr/bin/env pypy
import sys
import math

if len(sys.argv) < 2:
    print("Not enough params")

data = []

with open(sys.argv[1], 'r') as f:
    # 3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
    rows, columns, vehicles, rides, bonus, steps = [int(x) for x in f.readline()[0:-1].split(" ")]
    lines = f.readlines()
    for line in lines:
        vals = [int(x) for x in line[0:-1].split(" ")]
        start = vals[0:2]
        end = vals[2:4]
        earlyStart = int(vals[4])
        earlyEnd = int(vals[5])
        data.append([start, end, earlyStart, earlyEnd])

rideVehi = int(math.ceil(float(rides) / float(vehicles)))

for i in range(vehicles):
    tmp = range(i,rides,vehicles)
    sys.stdout.write(str(len(tmp))+ " " )
    for i in tmp:
        sys.stdout.write(str(i) + " ")
    sys.stdout.write("\n")
    