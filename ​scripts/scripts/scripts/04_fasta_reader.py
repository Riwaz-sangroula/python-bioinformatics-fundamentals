def read_fasta(filename):
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line.startswith(">"):
                sequence += line

    return sequence


dna = read_fasta("example_sequence.fasta")

print("Sequence:", dna)
print("Length:", len(dna))
