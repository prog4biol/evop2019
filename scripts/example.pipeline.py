#!/usr/env/python3
import subprocess
import sys

blastcmd = "blastx -query test.query -db ~/dbs/uniprot_sprot.fasta -outfmt 7 -out test.blastout.tab -evalue 1e-5"
countcmd = 'grep \'hits found\' test.blastout.tab  | perl -ne \'m/(\d+)/; $count=$1; print $count,"\n"'

blastcmd_run = subprocess.run(blastcmd, shell=True , stdout = subprocess.PIPE, stderr=subprocess.PIPE)
if blastcmd_run.returncode == 0:
  countcmd_run = subprocess.run(countcmd,  shell=True , stdout = subprocess.PIPE, stderr=subprocess.PIPE)
else:
   sys.exit("BLAST had issues " + blastcmd_run.stderr.decode('utf-8'))

  
if countcmd_run.returncode == 0:
  if countcmd_run.stdout.decode('utf-8') > 0:
    # parse results
    print("We will put parsing code here")
  else:
    sys.exit("no hits")
else:
  sys.exit("count had issues " + countcmd_run.stderr.decode('utf-8'))

