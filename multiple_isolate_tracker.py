def main():
    isolates_dict = {}
    while True:
        try:
            name = input("Isolate Name: ").title().strip()
            antibiotic = input("Antibiotic Name: ").title().strip()
            zone = float(input("Zone(mm): "))
            print(add_isolate(isolates_dict, name, antibiotic, zone))
        except EOFError:
            break
def add_isolate(isolates_dict, name, antibiotic, zone):
    isolates_dict.setdefault(name,{})
    isolates_dict[name][antibiotic] = zone    #dict[key] = value adds to a dict
    return isolates_dict
if __name__ == "__main__":
    main()
