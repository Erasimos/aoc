import ut
import re

NR_GREENS = 13
NR_BLUES = 14
NR_REDS = 12 

def get_input():
    puzzle_input = ut.read_file()
    games = []
    for line in puzzle_input:
        game = {}
        sets = re.split(':|;', line)
        game['id'] = int(sets[0].split()[1])
        game_sets = [] 
        for set in sets[1:]:
            game_set = []
            for pair in set.split(','):
                set_pair = {}
                set_pair['number'] = int(pair.split()[0])
                set_pair['color'] = pair.split()[1]
                game_set.append(set_pair)
            game_sets.append(game_set)
        game['sets'] = game_sets
        games.append(game)
    return games


# Returns 0 if game is impossible, otherwise the game id
def validate_game(game: dict):

    game_id = game['id']

    for set in game.get('sets', []):

        for pair in set:
            color = pair.get('color', '')
            number = pair.get('number', 0)

            if color == 'red' and number > NR_REDS:
                return 0

            elif color == 'blue' and number > NR_BLUES:
                return 0
                
            elif color == 'green' and number > NR_GREENS:
                return 0
            
    return game_id


def get_minimum_required_cubes(game: dict):

    min_reds = 0
    min_greens = 0
    min_blues = 0

    for set in game.get('sets', []):
        for pair in set:
            color = pair.get('color', '')
            number = pair.get('number', 0)

            if color == 'red':
                min_reds = max(min_reds, number)

            elif color == 'blue':
                min_greens = max(min_greens, number)
                
            elif color == 'green':
                min_blues = max(min_blues, number)
    
    return min_reds * min_greens * min_blues
            


def part_one():

    games = get_input()

    answer = 0

    for game in games:
        answer += validate_game(game)

    ut.print_answer(part=1, day='template', answer=answer)


def part_two():

    games = get_input()

    answer = 0

    for game in games:
        answer += get_minimum_required_cubes(game)

    ut.print_answer(part=2, day='template', answer=answer)


part_one()
part_two()