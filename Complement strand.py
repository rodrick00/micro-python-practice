def main():
    x = input("DNA Strand: ").upper()
    print(f"{complement(x)}")
def complement(dna):
    strand_dict = {"A":"T","T":"A","G":"C","C":"G"}
    complementary_dna = ""
    for one_dna in dna:
        complementary_dna = complementary_dna + strand_dict[one_dna]
    return complementary_dna
if __name__ == "__main__":
    main()
