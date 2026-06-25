import re
def main():
    s = input("Accession number: ").strip().upper()
    print(is_valid_accession(s))
def is_valid_accession(s):
    matches =  re.fullmatch(r"([A-Z]{2})(\d{6})",s)
    if matches:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
