def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("both sequences must have the same size.")

    differences = 0
    for seq in range(len(strand_a)):
        if strand_a[seq] != strand_b[seq]:
            differences += 1

    return differences
