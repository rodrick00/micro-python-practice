def main():
    x ='ATGATG' #enter string here
    k = 3
    print(find_repeats(x, k))
def find_repeats(dna, k):
    counts = {}
    for i in range(len(dna)):
        sub_string = dna[i:i+k]
        if sub_string in counts:
            counts[sub_string] = counts[sub_string] + 1
        else:
            counts[sub_string] = 1
    empty = []
    for evry_sub in counts:
        if counts[evry_sub]> 1:
            empty.append(evry_sub)
    return empty
if __name__ == "__main__":
    main()
