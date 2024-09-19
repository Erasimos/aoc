import ut
import re

def get_input():
    puzzle_input = ut.read_file()[0].split(',')
    return puzzle_input


def custom_hash(str):
    
    value = 0

    for char in str:
        value = ((value + ord(char)) * 17) % 256
    return value

def part_one():

    input = get_input()
    hash_values = [custom_hash(el) for el in input]
    answer = sum(hash_values)

    ut.print_answer(part=1, day=15, answer=answer)


def get_init_sequence(input):
    pattern = r"([a-zA-Z]+)([=-])(\d*)"
    init_sequence = [[match.group(1), match.group(2), match.group(3)] for el in input if (match := re.match(pattern, el))]
    return init_sequence


def run_init_sequence(init_sequence):
    boxes = {i: {} for i in range(256)}

    for lens_label, operation, *rest in init_sequence:

        box_id = custom_hash(lens_label)
        lens_box = boxes[box_id]

        if operation == '-':
            lens_box.pop(lens_label, None)

        elif operation == '=' and rest:
            lens_box[lens_label] = int(rest[0])
            
    return boxes


def calculate_focus_power(boxes: dict):
    
    total_focus_power = 0

    for box_i, box in enumerate(boxes.values(), start=1):
        for slot_i, focal_l in enumerate(box.values(), start=1):
            total_focus_power += box_i * slot_i * focal_l

    return total_focus_power

def part_two():

    input = get_input()
    init_seq = get_init_sequence(input)
    boxes = run_init_sequence(init_sequence=init_seq)
    answer = calculate_focus_power(boxes=boxes)
    ut.print_answer(part=2, day='15', answer=answer)


part_one()
part_two()