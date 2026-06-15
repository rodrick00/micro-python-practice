def main():
    with_inh = get_input("Zone with inhibitor(mm): ")
    without_inh = get_input("Zone without inhibitor(mm): ")
    print(with_inh,without_inh)
def get_input(prompt):
    while True:
        try:
            both_values = float(input(prompt))
            if both_values <= 0:
                print("enter values greater than 0")
                continue
            return both_values

        except ValueError:
            print("Enter numbers only!")
            continue
if __name__ == "__main__":
    main()
