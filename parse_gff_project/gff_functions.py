def read_fasta(fasta_file):
    """
    Reads a FASTA file and returns a single DNA string.
    """
    file = open(fasta_file, "r")

    # skip header line
    next(file)

    genome_sequence = ""

    for line in file:
        genome_sequence += line.strip()

    file.close()

    print("Genome length:", len(genome_sequence))
    return genome_sequence


def read_gff(gff_file, genome_sequence):
    """
    Reads GFF file and extracts sequences using coordinates.
    Returns a list of (sequence_id, sequence).
    """
    features = []

    file = open(gff_file, "r")

    for line in file:
        # skip comments
        if line.startswith("#"):
            continue

        parts = line.strip().split("\t")

        start = int(parts[3]) - 1
        end = int(parts[4])

        info = parts[8]

        # extract ID
        seq_id = ""
        for item in info.split(";"):
            if item.startswith("ID="):
                seq_id = item[3:]

        # slice genome
        sequence = genome_sequence[start:end]

        features.append((seq_id, sequence))

    file.close()

    print("Total features extracted:", len(features))
    return features


def write_output(features, output_file):
    """
    Writes extracted sequences to a FASTA file.
    """
    file = open(output_file, "w")

    for seq_id, sequence in features:
        file.write(">" + seq_id + "\n")
        file.write(sequence + "\n")

    file.close()

    print("FASTA file written:", output_file)