class BacterialIsolate:
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.zones = {}
    def add_zone(self,antibiotic, mm):
        self.zones[antibiotic] = mm
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
if __name__ == "__main__":
    main()
