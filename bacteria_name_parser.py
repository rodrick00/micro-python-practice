import re
def main():
    name = input("Bacterial Name: ").strip()
    print(parse_bacteria_name(name))

def parse_bacteria_name(name):
    matches =  re.search(r"^([A-Z][a-z]+) ([a-z]+)$",name)
    if matches:
        genus = matches.group(1)
        species = matches.group(2)
        return (genus, species)
    else:
        raise ValueError("Invalid")
if __name__ == "__main__":
    main()
