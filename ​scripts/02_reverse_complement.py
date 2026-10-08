dna = "ATGCGTAC"

complement = ""

for base in dna:
    if base == "A":
        complement += "T"
    elif base == "T":
        complement += "A"
    elif base == "G":
        complement += "C"
    elif base == "C":
        complement += "G"

reverse_complement = complement[::-1]

print("DNA:", dna)
print("Complement:", complement)
print("Reverse complement:", reverse_complement)
