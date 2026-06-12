def main():
    codon= input("DNA Strand: ").upper()
    print(f"Translated Amino Acid: {translate(codon)}")
def translate(codon):
    strand_dict = {"ATG":"Met","TAA":"Stop","GCT":"Ala","TGG":"Trp"}
    if codon not in strand_dict:
        return "Unknown"
    else:
        return strand_dict[codon]
if __name__ == "__main__":
    main()
