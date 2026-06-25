class EffluxResult:
    def __init__(self, antibiotic, with_inh, without_inh):
        self.antibiotic = antibiotic
        self.with_inh = with_inh
        self.without_inh = without_inh
    @property
    def difference(self):
        zone_diff =  self.with_inh - self.without_inh
        return zone_diff
    @property
    def is_active(self):
        if self.difference >= 2:
            return True
        else:
            return False
    def __str__(self):
        return f"{self.antibiotic}. Zones: {self.with_inh}, {self.without_inh}"

def main():
    user_antibiotic = input("Antibiotic Name: ").strip().title()
    user_zone_with = float(input("Zone with Inhibitor: "))
    user_zone_without = float(input("Zone without Inhibitor: "))
    result = EffluxResult(user_antibiotic, user_zone_with,user_zone_without)
    print(result)
    print(result.difference)
    print(result.is_active)

if __name__ == "__main__":
    main()
