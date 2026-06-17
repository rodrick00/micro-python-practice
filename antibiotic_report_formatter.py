def main():
    x = {'Ampicillin': 'Resistant', 'Tetracycline': 'Sensitive'}
    print(format_report(x))
def format_report(results_dict):
    sorted_list = []
    for antibiotic, classification in sorted(results_dict.items()):
        sorted_list.append(f"{antibiotic} : {classification}")
    return "\n".join(sorted_list)
if __name__ == "__main__":
    main()
