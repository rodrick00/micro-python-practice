def main():
    x = 'Ampicillin,12,18\nTetracycline,17,19'
    print(parse_csv(x))
def parse_csv(data):
    new_line = data.split("\n")
    whole_data = []
    for rows in new_line:
        raw_data = rows.split(",")
        second_position = int(raw_data[1])
        third_position = int(raw_data[2])
        create_tuple = (raw_data[0],second_position,third_position)
        whole_data.append(create_tuple)
    return whole_data
if __name__ == "__main__":
    main()
