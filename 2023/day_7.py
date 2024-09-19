import ut

hand_type_ranking = {
    'High card': 0,
    'One pair': 1, 
    'Two pair': 2,
    'Three of a kind': 3,
    'Full house': 4,
    'Four of a kind': 5,
    'Five of a kind': 6
}

def get_type_joker(hand):

    best_hand_type_ranking = 0
    best_hand_type = 'One pair'

    if not 0 in hand:
        hand_type = get_type(hand)
        if hand_type_ranking[hand_type] > best_hand_type_ranking:
            return hand_type

    else:
        for index, card in enumerate(hand):
            if card == 0:
                for card_val in [1,2,3,4,5,6,7,8,9,10,12,13,14]:
                    new_hand = hand.copy()
                    new_hand[index] = card_val
                    
                    hand_type = get_type_joker(new_hand)
                    if hand_type_ranking[hand_type] > best_hand_type_ranking:
                        best_hand_type_ranking = hand_type_ranking[hand_type]
                        best_hand_type = hand_type

    return best_hand_type               


def get_type(hand):

    card_1 = hand[0]
    card_2 = hand[1]
    card_3 = hand[2]
    card_4 = hand[3]
    card_5 = hand[4]

    card_set = {card_1, card_2, card_3, card_4, card_5}
    card_set_length = len(card_set)

    # Five of a kind
    if card_set_length == 1 :
        return 'Five of a kind'

    # Full house and Four of a kind
    elif card_set_length == 2:
        for index, card in enumerate(hand):
            matches = 1
            if index + 1 < len(hand):
                for compare_card in hand[index + 1:]:
                    if card == compare_card:
                        matches += 1
                        if matches == 4: 
                            return 'Four of a kind'
                        
        return 'Full house'

    # Two pair and Three of a kind
    elif card_set_length == 3:
        for index, card in enumerate(hand):
            matches = 1
            if index + 1 < len(hand):
                for compare_card in hand[index + 1:]:
                    if card == compare_card:
                        matches += 1
                        if matches == 3: 
                            return 'Three of a kind'

        return 'Two pair'

    # One pair
    elif card_set_length == 4:
        return 'One pair'

    # High card
    elif card_set_length == 5:
        return 'High card'


# returns true if hand_1 beats hand_2
def beats(hand_1, hand_2):
    type_1 = hand_1['type']
    type_2 = hand_2['type']
    hand_type_ranking_1 = hand_type_ranking[type_1]
    hand_type_ranking_2 = hand_type_ranking[type_2]

    if hand_type_ranking_1 > hand_type_ranking_2:
        return True
    elif hand_type_ranking_1 == hand_type_ranking_2:
        # Hands have the same type
        for index, card_h1 in enumerate(hand_1['hand']):
            card_h2 = hand_2['hand'][index]

            if card_h1 > card_h2:
                return True
            elif card_h1 < card_h2:
                return False
    else:
        return False


def sort_hands(hands):
    sorted_hands = []
    for hand in hands:

        

        if sorted_hands == []:
            sorted_hands.append(hand)

        else:

            inserted = False

            for index, sorted_hand in enumerate(sorted_hands):

                if beats(hand, sorted_hand):
                    sorted_hands = sorted_hands[0:index]  + [hand] + sorted_hands[index:]
                    inserted = True
                    break

            if not inserted:
                sorted_hands = sorted_hands + [hand]

    sorted_hands.reverse()
    return sorted_hands                


def get_winnings(sorted_hands):

    winnings = 0

    for index, hand in enumerate(sorted_hands):
        bid = hand['bid']
        winnings += (bid * (index + 1))

    return winnings


def get_hands(wilcards=False):
    hands = []
    puzzle_input = ut.read_file()
    for line in puzzle_input:
        hand_dict = {}
        hand = []

        contains_joker = False

        for card in line.split()[0]:

            

            if str.isnumeric(card):
                hand.append(int(card))
            else:
                if card == 'A':
                    card_value = 14
                elif card == 'K':
                    card_value = 13
                elif card == 'Q':
                    card_value = 12
                elif card == 'J':
                    contains_joker = True
                    if wilcards:
                        card_value = 0
                    else:
                        card_value = 11
                elif card == 'T':
                    card_value = 10

                hand.append(card_value)


             
        bid = int(line.split()[1])

        hand_dict['hand'] = hand
        hand_dict['bid'] = bid

        if contains_joker and wilcards:
            hand_dict['type'] = 'One pair'
            hand_dict['type'] = get_type_joker(hand)
        else:
            hand_dict['type'] = get_type(hand)

        

        hands.append(hand_dict)

    return hands



def part_one():

    hands = get_hands()
    sorted_hands = sort_hands(hands)
    winnings = get_winnings(sorted_hands)
    ut.print_answer(part=1, day='7', answer=winnings)


def part_two():

    hands = get_hands(wilcards=True)
    sorted_hands = sort_hands(hands)
    winnings = get_winnings(sorted_hands)
    ut.print_answer(part=2, day='7', answer=winnings)

part_one()
part_two()