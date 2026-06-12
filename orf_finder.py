def main():
    x = input("DNA starnd: ").upper().strip()
    print(f"'ATG' in given DNA: {has_start_codon(x)}"),
    print(f"'TAA', 'TAG', or 'TGA' in given DNA: {has_stop_codon(x)}")
def has_start_codon(dna):
     if 'ATG' in dna:
        return True
     else:
         return False
def has_stop_codon(dna):
    if 'TAA' in dna or  'TAG' in dna or 'TGA' in dna:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
