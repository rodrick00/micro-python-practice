def main():
    x = input("FASTA line: ").upper()
    print(parse_fasta_line(x))
def parse_fasta_line(line):
    if line.startswith(">"):
        return "header"
    else:
        return "sequence"
if __name__ == "__main__":
    main()
