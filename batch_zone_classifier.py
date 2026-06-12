from zone_classifier import classify_zone
def main():
    full_data = {'Ampicillin': 12, 'Tetracycline': 17}
    final_result = classify_all(full_data)
    print(final_result)
def classify_all(zone_dict) :
    new_dict = {}
    for every_antibiotic in zone_dict:
        size_of_zone = zone_dict[every_antibiotic]
        classification_of_antibiotic = classify_zone(size_of_zone)
        new_dict[every_antibiotic] = classification_of_antibiotic
    return new_dict
if __name__ == "__main__":
    main()
