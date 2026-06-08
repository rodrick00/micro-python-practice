def main():
      dna = input("DNA bases: ").upper()
      print(F"RESULT {count_bases(dna)}")

def count_bases(dna):
      storing_bases_count = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
      for one_dna in dna:
            if one_dna not in storing_bases_count:
                  continue
            storing_bases_count[one_dna] = storing_bases_count[one_dna] + 1
      return storing_bases_count
if __name__ == "__main__":
      main()
