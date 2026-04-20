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
    features = []

    file = open(gff_file, "r")

    for line in file:
        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")

        start = int(parts[3]) - 1
        end = int(parts[4])

        info = parts[8]

        seq_id = ""
        for item in info.split(";"):
            if item.startswith("ID="):
                seq_id = item[3:]

        sequence = genome_sequence[start:end]

        features.append((seq_id, sequence))

    file.close()

    print("Total features:", len(features))
    return features

def write_output(features, output_file):
    file = open(output_file, "w")

    for f in features:
        file.write(">" + f[0] + "\n")
        file.write(f[1] + "\n")

    file.close()

    print("Output file created")