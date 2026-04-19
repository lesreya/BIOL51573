#!/usr/bin/env python3

import argparse
from gff_functions import read_fasta, read_gff, write_output


def main():
    parser = argparse.ArgumentParser(description="Parse GFF and extract sequences")

    parser.add_argument("fasta", help="Input FASTA file")
    parser.add_argument("gff", help="Input GFF file")

    args = parser.parse_args()

    genome_sequence = read_fasta(args.fasta)
    features = read_gff(args.gff, genome_sequence)

    output_file = "covid_genes.fasta"
    write_output(features, output_file)

    print(f"Output written to {output_file}")


if __name__ == "__main__":
    main()
