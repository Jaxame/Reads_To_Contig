'''
 # @ Author: AME Jacky
 # @ Creation: 2022-11-23 16:05:35
'''
from read import *
from contig import *

with open("dna_reads.txt", "r") as file:
    reads = [line.strip().upper() for line in file]
    lreads = [Read(read) for read in reads]
    contig1 = Contig(lreads[0].get_seq())
    print(lreads[0])
    print(contig1)
