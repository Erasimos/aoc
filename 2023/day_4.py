import ut

def get_scratchcards():
    puzzle_input = ut.read_file()

    scrachcards = []

    for line in puzzle_input:
        split_line = line.split(sep=':')

        split_line = split_line[1].split('|')

        owned_numbers = [int(el) for el in split_line[0].split()]
        winning_numbers = [int(el) for el in split_line[1].split()]

        card = {}
        card['copies'] = 1
        card['owned_numbers'] = owned_numbers
        card['winning_numbers'] = winning_numbers
        scrachcards.append(card)

    return scrachcards


def get_card_points(card):
    
    owned_numbers = card['owned_numbers']
    winning_numbers = card['winning_numbers']

    score = 0

    for number in owned_numbers:
        if number in winning_numbers:
            if not score == 0:
                score *= 2
            else: 
                score = 1
    
    return score


def score_cards(scratchcards):

    for index, card in enumerate(scratchcards):

        owned_numbers = card['owned_numbers']
        winning_numbers = card['winning_numbers']

        copies = card['copies']

        for i in range(copies):

            matches = 0

            for number in owned_numbers:
                if number in winning_numbers:
                    matches += 1

            for j in range(matches):
                card_index = index + j + 1
                if card_index >= len(scratchcards):
                    break
                else:
                    scratchcards[card_index]['copies'] = scratchcards[card_index]['copies'] + 1


def part_one():

    scratchcards = get_scratchcards()

    total_points = 0
    for card in scratchcards:
        total_points += get_card_points(card)


    ut.print_answer(part=1, day=4, answer=total_points)
    


def part_two():

    scratchcards = get_scratchcards()
    score_cards(scratchcards)
    
    total_scratchcards = sum([card['copies'] for card in scratchcards])

    ut.print_answer(part=2, day=4, answer=total_scratchcards)



part_one()
part_two()