#!/usr/bin/env python3

import argparse

from gff_functions import read_gff

read_gff(args.gff, genome)

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
parser.add_argument("gff")

args = parser.parse_args()

features = read_gff(args.gff, genome)

print("FASTA:", args.fasta)
print("GFF:", args.gff)