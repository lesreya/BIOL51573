def read_fasta(fasta_file):
    file = open(fasta_file, "r")
    next(file)

    genome = ""
    for line in file:
        genome += line.strip()

    file.close()

    print("Genome length:", len(genome))
    return genome
