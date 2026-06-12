def main():
    x = int(input("Zone Of Inhibition: "))
    print(f"Classification: {classify_zone(x)}")
def classify_zone(mm):
    if mm <= 14:
        return "Resistant"
    elif 15<= mm <=19:
        return "Intermediate"
    else :
        return "Sensitive"
if __name__ == "__main__":
    main()
