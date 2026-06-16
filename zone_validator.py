def main():
    x = float(input ("Zone WITH Inhibition: "))
    y = float(input ("Zone WITHOUT Inhibition: "))
    print(validate_zone_pair(x, y))
def validate_zone_pair(with_inh, without_inh):
    if with_inh < 0 or without_inh < 0:
        raise ValueError("Values cannot be negative.Please Enter a valid number!")
    if with_inh == 0 or without_inh == 0:
        raise ValueError("Values cannot be zero.Please Enter a valid number!")
    if without_inh > with_inh:
        raise ValueError("Zone Without Inhibitor cannot be Greater than zone With Inhibitor.Please Enter a valid number!")
if __name__ == "__main__":
    main()
