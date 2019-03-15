#!/usr/bin/env python3

import re	                                          # Import regular expressions

seq_read = open("sequence_data.txt", "r")	          # Open the file

genes = {}	                                        # Create your -empty- dictionary

for line in seq_read:		                            # Read the file line by line
	line = line.rstrip()	                            # Remove "end of line" (\n) from the line
	id,seq = line.split()	                            # Split the line in gene name (id) and its sequence (seq)
	codons = re.findall(r"(.{3})",seq)	              # Find all the codons
	count_codons = len(codons)	                      # Count the number of codons in the list
	print(id, "\t", count_codons)	                    # Print gene name and codon count

seq_read.close()	                                  # Always close your file
