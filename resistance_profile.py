class BacterialIsolate:
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.zones = {}
    def add_zone(self,antibiotic, mm):
        self.zones[antibiotic] = mm
    def resistance_profile(self):
         resistance_profile = {}
         for antibiotic, mm in self.zones.items():
            if mm <= 14:
                resistance_profile[antibiotic] = "Resistant"
            elif 15 <= mm <= 19:
                resistance_profile[antibiotic] = "Intermediate"
            else:
                resistance_profile[antibiotic] = "Sensitive"
         return resistance_profile

    def __str__(self):
        return f"{self.name} from {self.source}. Zones: {self.zones}"

def main():
    user_name = input("Bacteria Name: ").strip()
    user_source = input("Isolated From (Source): ").strip()
    isolate = BacterialIsolate(user_name, user_source)
    antibiotic = input("Antibiotic Name: ").title().strip()
    mm = float(input("Zone(mm): "))
    isolate.add_zone(antibiotic, mm)
    print(isolate)
    print(isolate.resistance_profile())
if __name__ == "__main__":
    main()
