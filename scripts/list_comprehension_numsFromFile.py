#!/usr/bin/env python3

fh = open("nums.txt")

for line in fh:
  line = line.rstrip()
  values = [float(x) for x in line.split("\t")]
  print(values)
