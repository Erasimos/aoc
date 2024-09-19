import ut


def get_records():
    puzzle_input = ut.read_file()
    times = [int(el) for el in puzzle_input[0].split() if str.isnumeric(el)]
    distances = [int(el) for el in puzzle_input[1].split() if str.isnumeric(el)]
    records = list(zip(times, distances))    
    return records

def find_intersections(time, distance):

    # Start search in the middle

    wait_step = int(time / 2)
    wait = wait_step

    while True:
        

        wait_step = max(int(wait_step / 2), 1)

        new_distance = wait * (time - wait)
        new_distance_minus_one = (wait - 1) * (time - (wait - 1))

        if new_distance > distance and new_distance_minus_one < distance:
            break
        elif new_distance > distance:
            
            wait = wait - wait_step 
        else:
            wait = wait + wait_step

    intersection_1 = wait
    intersection_2 = time - wait

    return intersection_1, intersection_2


def race(time, wait):
    speed = wait
    time_left = time - wait

    distance = speed * time_left
    return distance

def find_winning_ways(time, distance):

    ways = []

    for wait in range(time):
        new_distance = race(time, wait)
        if new_distance > distance:
            ways.append(wait)

    return ways

def part_one():

    records = get_records()

    answer = 1

    for record in records:
        time = record[0]
        distance = record[1]


        winning_ways = find_winning_ways(time, distance)

        answer *= len(winning_ways)

    ut.print_answer(part=1, day='6', answer=answer)


def part_two():

    records = get_records()

    time = ''
    distance = ''

    for record in records:
        time += str(record[0])
        distance += str(record[1])

    time = int(time)
    distance = int(distance)

    intersection_1, intersection_2 = find_intersections(time, distance)
        
    answer = intersection_2 - intersection_1 + 1

    ut.print_answer(part=2, day='template', answer=answer)



part_one()
part_two()
