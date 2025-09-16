def to_rna(dna_strand):
    key = {'G':'C', 'C':'G', 'T': 'A', 'A': 'U'}
    result = ""
    for dna in dna_strand:
        result += key[dna]

    return result

