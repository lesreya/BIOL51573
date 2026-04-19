def read_fasta(fasta_file):
    genome_sequence = ""

    file = open(fasta_file, "r")

    # skip first line (header)
    next(file)

    for line in file:
        line = line.strip()
        genome_sequence = genome_sequence + line

    file.close()

    return genome_sequence


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

        # find ID
        items = info.split(";")
        seq_id = ""

        for item in items:
            if item.startswith("ID="):
                seq_id = item[3:]   # remove "ID="

        sequence = genome_sequence[start:end]

        features.append((seq_id, sequence))

    file.close()

    return features


def write_output(features, output_file):
    file = open(output_file, "w")

    for feature in features:
        seq_id = feature[0]
        sequence = feature[1]

        file.write(">" + seq_id + "\n")
        file.write(sequence + "\n")

    file.close()