def read_fasta(fasta_file):
    file = open(fasta_file, "r")
    next(file)

    genome = ""
    for line in file:
        genome += line.strip()

    file.close()

    print("Genome length:", len(genome))
    return genome

def read_gff(gff_file, genome_sequence):
    file = open(gff_file, "r")

    for line in file:
        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")
        start = int(parts[3]) - 1
        end = int(parts[4])

        sequence = genome_sequence[start:end]

        print("Extracted sequence preview:", sequence[:20])
