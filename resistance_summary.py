def main():
    x = ['Resistant','Sensitive','Resistant','Intermediate'] # ENTER YOUR LIST
    classify,percent = resistance_summary(x)
    print(classify)
    print(f"Resistant Percentage: {percent}%")
def resistance_summary(classifications):
    counts = {}
    for every_category in classifications:
        if every_category in counts:
            counts[every_category] = counts[every_category] + 1 
        else:
            counts[every_category] = 1 
        percentage = (counts["Resistant"]/len(classifications))*100
    return counts,percentage
if __name__ == "__main__":
    main()
