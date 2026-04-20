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
        print("Start:", parts[3], "End:", parts[4])
        break

    file.close()
