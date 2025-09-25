rna_strands = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyrosine",
    "UAC" : "Tyrosine",
    "UGU" : "Cysteine",
    "UGC" : "Cysteine",
    "UGG" : "Tryptophan",
    "UAA" : "STOP",
    "UAG" : "STOP",
    "UGA" : "STOP"
}
def proteins(strand):
    strand_list = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []
    for i in strand_list:
        if rna_strands[i] == 'STOP':
            break
        result.append(rna_strands[i])
    return result
