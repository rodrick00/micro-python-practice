def main():
    seq1 = input("DNA Sequence: ").upper().strip()
    seq2 = input("DNA Sequence: ").upper().strip()
    print(find_mutations(seq1, seq2))
def find_mutations(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Length of both sequences differ")
    mutation_at = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutation_at.append(i)
    return mutation_at
if __name__ == "__main__":
    main()
