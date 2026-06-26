import csv
def main():
    filename = input("Filename: ")
    print(read_antibiogram_csv(filename))

def read_antibiogram_csv(filename):
    antibiogram = {}
    try:
        with open (filename) as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                isolate  = row[0]
                antibiotic = row[1]
                zone_mm  = float(row[2])
                antibiogram.setdefault(isolate, {})
                antibiogram[isolate][antibiotic] = zone_mm
            return antibiogram
    except FileNotFoundError:
        return "File Not Found"
if __name__ == "__main__":
    main()
