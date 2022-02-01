# Exercise 6. k-mer counting (1/2)
#
# (1/2)
# Remember the previous exercise of finding (unique) substrings of length 3.
# - Make a function from your implementation.
# - Have k as an argument to the function.
# (2/2)
# Modify your function to use a dictionary with substring counts.
# - Use the substrings as dictionary keys.
# - Use the counts as dictionary values.
# - Have the function return the dictionary.
# - Add a docstring to the function.


def substrings(dna_string, k=3):
    """
    Prints all length k substrings of the dna_string.
    """
    for i in range(0, len(dna_string) - k + 1):
        print(dna_string[i:i + k])


# Test the substrings function on several inputs.
dna_seq = "ACGT" * 3 + "TTATT" * 5

substrings(dna_seq)
substrings(dna_seq, k=5)


def kmer_counts(dna_string, k=3):
    """
    Modified version of substrings that returns a dictionary with
    it's keys the kmer sequences and as values their occurrence.
    """
    counts = {}
    for i in range(0, len(dna_string) - k + 1):
        kmer = dna_string[i:i + k]
        if kmer in counts:
            counts[kmer] += 1
        else:
            counts[kmer] = 1
    return counts


# Use the function to print k-mer counts for some strings.
counts = kmer_counts(dna_seq)
for kmer in counts:
    print('{0} occurs {1} time(s)'.format(kmer, counts[kmer]))
