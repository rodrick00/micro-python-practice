def main():
    m = int(input("MIC Value: "))
    b = int(input("Breakpoint Value: "))
    if is_resistant(m, b):
        print("Resistant")
    else:
        print("Sensitive")
def is_resistant(mic, breakpoint):
    if mic >= breakpoint:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
