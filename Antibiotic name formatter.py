def main():
    name = input("Antibiotic Name: ")
    print(f"Antibiotic Name: {format_name(name)}")
def format_name(name):
    return name.strip().title()
if __name__ == "__main__":
      main()
