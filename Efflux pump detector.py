def main():
    with_inh = float(input("Zone with inhibition(mm): "))
    without_inh = float(input("Zone without inhibition(mm): "))
    print(f"Efflux Active: {efflux_active(with_inh, without_inh)}")
def efflux_active(with_inh, without_inh):
    if with_inh <= 0 or without_inh <= 0:
        raise ValueError("Zones must be Greater than 0")
    difference = with_inh - without_inh
    if difference >= 2:
        return True
    else:
        return False
if __name__ == "__main__":
    main()
