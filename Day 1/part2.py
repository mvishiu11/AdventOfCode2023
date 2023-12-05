def get_calibration_values(line):
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    result_string = ''
    temp = ''

    # Replace spelled-out digits with actual digits
    for char in line:
        if not char.isalpha():
            result_string += char
        else:
            temp += char
            for digit in digits:
                if digit in temp:
                    result_string += digits[digit]
                    temp = temp.replace(digit, temp[-1])
    
    # Extract the first and last digits
    first_digit = result_string[0]
    last_digit = result_string[-1]

    # Convert to a two-digit number
    calibration_value = int(first_digit + last_digit)

    return calibration_value

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # Calculate calibration values for each line
    calibration_values = [get_calibration_values(line.strip()) for line in lines]

    # Sum up all calibration values
    total_sum = sum(calibration_values)

    print(f"The sum of all calibration values is: {total_sum}")

if __name__ == "__main__":
    main()