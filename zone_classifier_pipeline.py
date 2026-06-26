def main():
    name = input("Isolate Name: ").title().strip()
    zones = {}
    while True:
        antibiotic = input("Antibiotic (or 'done' to stop): ").strip().title()
        if antibiotic == "Done":
            break
        mm = float(input("Zone (mm): "))
        zones[antibiotic] = mm        
    print(analyze_isolate(name, zones))
def analyze_isolate(name, zones_dict):
    results = {}
    counts = {"Resistant": 0, "Intermediate": 0, "Sensitive": 0}
    for antibiotic, mm in zones_dict.items():
        if mm <= 14:
            classification = "Resistant"
        elif 15<= mm <=19:
            classification  = "Intermediate"
        else :
            classification = "Sensitive"
        results[antibiotic] = classification
        counts[classification] += 1
    resistance_rate = (counts["Resistant"] / len(zones_dict)) * 100
    return {"Isolate": name,
            "Results": results,
            "Counts": counts,
            "Resistance_rate": resistance_rate}
if __name__ == "__main__":
    main()
