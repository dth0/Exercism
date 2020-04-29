def to_rna(dna_strand):
    dict_seq = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    return "".join(
        [dict_seq[item.upper()] for item in dna_strand]
    )
