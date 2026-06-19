def main():
    isolates ={'Lactobacillus': {'Ampicillin': 12, 'Tetracycline': 15},'Salmonella': {'Penicillin': 19}} #add ur dict here
    antibiogram(isolates)
def antibiogram(isolates):
    for one_isolate in isolates:
        for one_antibiotic in isolates[one_isolate]:
            zone = isolates[one_isolate][one_antibiotic]
            if zone <= 14:
                classification = "Resistant"
            elif 15<= zone <=19:
                classification = "Intermediate"
            else :
                classification = "Sensitive"
            print(f"(isolate): {one_isolate:<20}: (Antibiotic Name): {one_antibiotic:<20} (Classification): {classification}")
if __name__ == "__main__":
    main()
