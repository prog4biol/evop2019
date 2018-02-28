#!/usr/bin/env python3

import sys
import pronto

GO_GENES = sys.argv[1]
MY_GO_ID = sys.argv[2]

# create an object of class Ontology with the GO ontology 
ont = pronto.Ontology('/Users/smr/Desktop/PFB2017/pfb2017/files/go.owl')

# get the term name of the provided GO ID
term_obj = ont[MY_GO_ID]
term_name = term_obj.name
print("These genes have all been annotated with" , MY_GO_ID + ', "' + term_name + '" or any of its child terms' )


# add the parent GO ID to dictionary of IDs to search for
all_children={}
all_children[MY_GO_ID] = term_name

# add all children of the parent term to dictionary
for child in ont[MY_GO_ID].rchildren():
  all_children[child.id] = child.name

# open genes file and add gene names and their annotatoted GO terms to a dictionary 
genes = {}
file = open(GO_GENES , "r")
for line in file:
  line = line.rstrip()
  columns = line.split("\t")
  # if a gene does not have a GO term annotation, skip it
  if len(columns) == 3:
    (gene_id , go_id, go_name) = columns
    if go_id in all_children:
      genes[gene_id] = go_id

# print out all the genes that are of the GO ID you provided as well as any of its children
for gene in genes:
   go_id = genes[gene]
   go_id_obj = ont[go_id]
   go_name = go_id_obj.name
   output = "\t".join( [gene,go_id,go_name] )
   print(output)
