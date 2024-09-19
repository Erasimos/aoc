import ut
import re

def get_input():
    puzzle_input = ut.read_file()
    return puzzle_input

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_first_and_last_digits_part_two(line):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|[1-9])'
    matches = []

    while line:
        match = re.search(pattern, line)
        if not match:
            break
        
        matches.append(match.group(0))
        line = line[match.start() + 1:]

    first_digit = matches[0] if matches[0].isnumeric() else word_to_digit[matches[0]]
    last_digit = matches[-1] if matches[-1].isnumeric() else word_to_digit[matches[-1]]

    calibration_value = int(first_digit + last_digit)
    
    return calibration_value

def find_first_and_last_digits_part_one(line):
    pattern = r'([1-9])'
    matches = re.findall(pattern, line)

    first_digit = matches[0] if matches[0].isnumeric() else word_to_digit[matches[0]]
    last_digit = matches[-1] if matches[-1].isnumeric() else word_to_digit[matches[-1]]

    calibration_value = int(first_digit + last_digit)
    
    return calibration_value

def part_one():

    input = get_input()
    calibration_values = [find_first_and_last_digits_part_one(line) for line in input]
    answer = sum(calibration_values)

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    input = get_input()
    calibration_values = [find_first_and_last_digits_part_two(line) for line in input]
    answer = sum(calibration_values)

    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()