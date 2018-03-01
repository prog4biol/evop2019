#!/usr/bin/env python3
import re
import sys

filename = sys.argv[1]
file = open(filename,'r')

seqs = {}
ID=''
for line in file:
  line = line.rstrip()
  header = re.search(r">(\S+)\s*(.*)",line)
  if header:
    if header.group(1):
      ID =  header.group(1)
  else:
    seq = line
    if ID in seqs:
      seqs[ID] += seq
    else:
      seqs[ID] = seq

## Now you have a dictionary of all your sequences
print(seqs)
for id in seqs:
  seq = seqs[id]
  print(id,seq)
