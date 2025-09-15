"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    result = [number]
    for i in range(1,3):
        result.append(number+i)
    return result


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    hand_length = len(hand)
    hand_sum = sum(hand)
    return hand_sum/hand_length


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    all_average = card_average(hand)
    first_last_avg = card_average([hand[0], hand[-1]])
    median_avg = hand[len(hand)//2]
    if all_average == first_last_avg or all_average == median_avg:
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_card = [hand[i] for i in range(0, len(hand),2)]
    odd_card = [hand[i] for i in range(1, len(hand),2)]
    avg_even = sum(even_card) / len(even_card)
    avg_odd = sum(odd_card) / len(odd_card)
    return avg_even == avg_odd


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
