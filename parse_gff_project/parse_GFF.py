#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fasta")
parser.add_argument("gff")

args = parser.parse_args()

print("FASTA:", args.fasta)
print("GFF:", args.gff)
