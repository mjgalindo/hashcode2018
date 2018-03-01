#!/usr/bin/env pypy
import sys


if len(sys.argv) < 2:
    print("Not enough params")

data = {}

with open(sys.argv[1], 'r') as f:
    # 3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
    rows, columns, vehicles, rides, bonus, steps = f.readline().split(" ")
    lines = f.readlines()
    for line in lines:
        vals = line.split(" ")



with open("result.txt", "w") as f:
    f.write("REsult")