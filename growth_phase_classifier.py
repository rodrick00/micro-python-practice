def main():
    x = float(input("How much time? ")) # enter in one decimal value
    print(classify_growth(x))
def classify_growth(hours):
    if 0.0 <= hours <= 2.0:
        return("lag phase")
    elif 2.0 < hours <= 8.0:
        return("exponential ")
    elif 8.0 < hours <= 16.0:
        return("stationary  phase")
    elif hours > 16.0:
        return ("death  phase")
if __name__ == "__main__":
    main()
