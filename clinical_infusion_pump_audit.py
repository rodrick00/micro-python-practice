def main():
    user_raw_numbers = input("Input all the Raw Readings separated by commas: ")
    raw_readings = [float(numbers) for numbers in user_raw_numbers.split(",")]
    print(f"Number of time dosage Elevated: {audit_pump_data(raw_readings)}")

def audit_pump_data(reading):
    elevated_count = 0
    for every_reading in reading:
        if every_reading < 0.0 or every_reading > 20.0:
            continue
        elif 10.0 <= every_reading <= 20.0:
            elevated_count = elevated_count + 1
        elif every_reading == 0.0:
            break
    return elevated_count

if __name__ == "__main__":
    main()
