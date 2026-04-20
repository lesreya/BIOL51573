#!/usr/bin/env python3

import argparse

from gff_functions import write_output

write_output(features, "covid_genes.fasta")

read_gff(args.gff, genome)

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
parser.add_argument("gff")

args = parser.parse_args()

features = read_gff(args.gff, genome)

print("FASTA:", args.fasta)
print("GFF:", args.gff)