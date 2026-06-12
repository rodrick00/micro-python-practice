def main():
    x = input("DNA Bases: ").upper()
    print(f"GC content: {gc_content(x)}%")
def gc_content(dna):
    total_gc = dna.count("G") + dna.count("C")
    total_len = len(dna)
    percentage = (total_gc /total_len)*100
    round_percentage = round(percentage,2)
    return round_percentage
if __name__ == "__main__":
    main()
