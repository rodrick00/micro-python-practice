from efflux_class import EffluxResult
class LabReport:
    def __init__(self):
        self.efflux_result = []
    def add_result(self,result):
        self.efflux_result.append(result)
    def summary(self):
        active = 0
        not_active = 0
        for result in self.efflux_result:
             if result.is_active:
                 active += 1
             else:
                 not_active += 1
        return f"ACTIVE: {active}, NOT ACTIVE: {not_active}"
    def __len__(self):
        total_no_of_results = len(self.efflux_result)
        return total_no_of_results
def main():
    report = LabReport()
    while True:
        user_antibiotic = input("Antibiotic Name: ").strip().title()
        if user_antibiotic == "Done":
            break
        else:
            user_zone_with = float(input("Zone with Inhibitor: "))
            user_zone_without = float(input("Zone without Inhibitor: "))
            result = EffluxResult(user_antibiotic, user_zone_with,user_zone_without)
            report.add_result(result)
    print(report.summary())
    print(f"Total Number Of Results: {len(report)}")
if __name__ == "__main__":
    main()
