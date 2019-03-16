#!/usr/bin/env python3

seq_read = open("sequence_data.txt", "r")	# Open the file
genes = {}	# Create your -empty- dictionary
for line in seq_read:		# Read the file line by line
	line = line.rstrip()	# Remove "end of line" (\n) from the line
	id,seq = line.split()	# Split the line in gene name (id) and its sequence (seq)
	genes[id]=  seq		# Add the new entry to the dictionary.

seq_read.close()	# Always close your file
print(genes)	# Lets see the dictionary :)
