dna = "ATGCGTAC"

print("DNA sequence:", dna)
print("Length:", len(dna))
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

gc_content = ((dna.count("G") + dna.count("C")) / len(dna)) * 100

print("GC content:", round(gc_content, 2), "%")
