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
  header = re.search(r"^>(\S+)\s*(.*)",line) 
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

file.close()

## Now you have a dictionary of all your sequences
seq_data = {}

print(seqs)
for id in seqs:
  seq = seqs[id]
  a_count = seq.count('A')
  t_count = seq.count('T')
  g_count = seq.count('G')
  c_count = seq.count('C')
  
  # we need to declare that the value of key->id is of type dictionary
  seq_data[id] = {}

  # we need to declare that the value of key->nt_comp is of type dictionary
  seq_data[id]['nt_comp'] = {}
  # adding keys to our nt_comp dict
  seq_data[id]['nt_comp']['A']= a_count
  seq_data[id]['nt_comp']['T']= t_count
  seq_data[id]['nt_comp']['G']= g_count
  seq_data[id]['nt_comp']['C']= c_count

  # we can just add a value to this key->seqlen
  seq_data[id]['seqlen'] = len(seq)
  
  # we can just add a value to this key->seq
  seq_data[id]['seq'] = seq

print(seq_data)
