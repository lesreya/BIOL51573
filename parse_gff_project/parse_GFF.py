#!/usr/bin/env python3

import argparse
from gff_functions import read_fasta, read_gff, write_output


def main():
    # Set up command line inputs
    parser = argparse.ArgumentParser(description="Parse GFF file and extract gene sequences")
    parser.add_argument("fasta", help="Input FASTA file")
    parser.add_argument("gff", help="Input GFF file")

    args = parser.parse_args()

    print("Reading genome...")
    genome = read_fasta(args.fasta)

    print("Parsing GFF and extracting sequences...")
    features = read_gff(args.gff, genome)

    print("Writing output FASTA file...")
    write_output(features, "covid_genes.fasta")

    # confirmation print statement
    print(f"Output saved to: {output_file}")

    print("Done!")


if __name__ == "__main__":
    main()