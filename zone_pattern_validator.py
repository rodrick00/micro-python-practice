import re
def main():
    s = input("Input Zone: ")
    print(is_valid_zone_string(s))

def is_valid_zone_string(s):
    if re.fullmatch(r"[1-9]\d?(\.\d)?",s):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
