def main():
    x = input("raw RNA sequence: ").upper()
    print(f"total protein count: {analyze_sequence(x)}")
def analyze_sequence(rna_strand):
    protein_count = 0
    for every_three_codon in range(0,len(rna_strand),3):
        codon = rna_strand[every_three_codon:every_three_codon+3]
        match codon:
            case "AUG":
                protein_count = protein_count+1
            case "UAA"| "UAG"| "UGA":
                break
            case _:
                continue
    return protein_count
if __name__ == "__main__":
    main()
