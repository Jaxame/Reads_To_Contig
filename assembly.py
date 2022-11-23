'''
 # @ Author: AME Jacky
 # @ Creation: 2022-11-23 16:05:35
'''
from read import *
from contig import *

with open("dna_reads.txt", "r") as file:
    lines = [line.strip().upper() for line in file]
    lreads = [Read(elt) for elt in lines]
    contig1 = Contig(lreads[0].get_seq())
    print(lreads[0])
    print(contig1)
