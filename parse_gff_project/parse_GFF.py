#!/usr/bin/env python3

import argparse

from gff_functions import read_fasta

genome = read_fasta(args.fasta)

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
parser.add_argument("gff")

args = parser.parse_args()

print("FASTA:", args.fasta)
print("GFF:", args.gff)
