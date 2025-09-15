"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'A':
        return 1
    if card in ('J','Q', 'K'):
        return 10
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_values = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 1
    }
    def get_value(card):
        if card in card_values:
            return card_values[card]
        return int(card)

    card_one_value = get_value(card_one)
    card_two_value = get_value(card_two)

    if card_one_value > card_two_value:
        return card_one
    elif card_two_value > card_one_value:
        return card_two
    else:
        return (card_one, card_two)

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == 'A' or card_two == 'A':
        return 1

    # Case 2: No Ace yet → pick best value
    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    ten_cards = {'10', 'J', 'Q', 'K'}
    return (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    card_values = {
        'J': 10, 'Q': 10, 'K': 10,
        'A': 11
    }
    def get_value(card):
        if card in card_values:
            return card_values[card]
        return int(card)
    # Convert cards to values
    val1 = get_value(card_one)
    val2 = get_value(card_two)
    return val1 == val2

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 1
    }

    total = card_values[card_one] + card_values[card_two]

    return total in (9, 10, 11)
