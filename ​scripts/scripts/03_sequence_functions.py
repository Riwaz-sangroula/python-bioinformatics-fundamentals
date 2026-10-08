def gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")

    return ((g + c) / len(dna)) * 100


def reverse_complement(dna):
    complements = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    complement = ""

    for base in dna:
        complement += complements[base]

    return complement[::-1]


sequence = "ATGCGTAC"

print("Sequence:", sequence)
print("GC content:", round(gc_content(sequence), 2), "%")
print("Reverse complement:", reverse_complement(sequence))
