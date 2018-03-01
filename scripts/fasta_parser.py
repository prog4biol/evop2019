#!/usr/bin/env python3
import re
import sys

# get filename from the command line 
filename = sys.argv[1]

# open the file
file = open(filename,'r')

# create an empty dictionary
seqs = {}

# create ab empty variable to hold the ID
ID=''

# go though the file line by line
for line in file:
  # remove the newline
  line = line.rstrip() 
  # use a regex to see if the line matches a FASTA header
  header = re.search(r">(\S+)\s*(.*)",line) 
  # if the line matches a FASTA header ...
  if header:
    # and if there is something stored in our first subpattern
    if header.group(1):
      # store the subpattern in the var ID
      ID =  header.group(1)
  # if the line must be sequence and not a header 
  else: 
    # lets make it obvious and save the line in a var called seq
    seq = line
    # check to see if we already have this ID in our dict
    if ID in seqs:
      # if we do, concatenate the new line to currently stored seq
      # same as seqs[ID] = seqs[ID] + seq
      seqs[ID] += seq
    # if we dont already have ID in our dict, we need to add it  
    else:
      seqs[ID] = seq

## Now you have a dictionary of all your sequences
print(seqs)
for id in seqs:
  seq = seqs[id]
  print(id,seq)
