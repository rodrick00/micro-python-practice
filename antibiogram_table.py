def main():
    isolates ={'Lactobacillus': {'Ampicillin': 12, 'Tetracycline': 15},'Salmonella': {'Penicillin': 19}} #add ur dict here
    antibiogram(isolates)
def antibiogram(isolates):
    print(f"{'Isolate':<20}{'Antibiotic':<20}{'Classification'}")
    for one_isolate in isolates:
        for one_antibiotic in isolates[one_isolate]:
            zone = isolates[one_isolate][one_antibiotic]
            if zone <= 14:
                classification = "Resistant"
            elif 15<= zone <=19:
                classification = "Intermediate"
            else :
                classification = "Sensitive"
            print(f"{one_isolate:<20}{one_antibiotic:<20}{classification}")
if __name__ == "__main__":
    main()

