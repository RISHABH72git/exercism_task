# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    if category == ONES:
        return calculate(dice, 1)
    elif category == TWOS:
        return calculate(dice, 2)
    elif category == THREES:
        return calculate(dice, 3)
    elif category == FOURS:
        return calculate(dice, 4)
    elif category == FIVES:
        return calculate(dice, 5)
    elif category == SIXES:
        return calculate(dice, 6)
    elif category == YACHT:
        return calculate_yatch(dice, dice[0])
    elif category == FULL_HOUSE:
        return calculate_fullhouse(dice)
    elif category == FOUR_OF_A_KIND:
        return calculate_four_of_a_kind(dice)
    elif category == LITTLE_STRAIGHT:
        return calculate_littile_straight(dice)
    elif category == BIG_STRAIGHT:
        return calculate_big_straight(dice)
    elif category == CHOICE:
        return calculate_choice(dice)
    else:
        return 0
def calculate_choice(dice):
    return sum(dice)
    
def calculate_big_straight(dice):
    if len(set(dice)) == 5:
        if 1 in dice:
            return 0
        else:
            return 30
    else:
        return 0
        
def calculate_littile_straight(dice):
    if len(set(dice)) == 5:
        if 6 in dice:
            return 0
        else:
            return 30
    else:
        return 0
        
def calculate_four_of_a_kind(dice):
    if len(set(dice)) > 2:
        return 0
        
    count = 0
    for i in dice:
        if i == dice[0]:
            count +=1
    if count == 1 or count == 5:
        dice.pop(0)
        return sum(dice)
    elif count == 4:
        return calculate(dice, dice[0])
    else:
        return 0
        
def calculate_yatch(dice, type):
    count = calculate(dice, type)
    if count == sum(dice):
        return 50
    else:
        return 0
        
def calculate_fullhouse(dice):
    if len(set(dice)) > 2 :
        return 0
    count = 0
    for i in dice:
        if i == dice[0]:
            count +=1
    if count == 2 or count == 3:
        return sum(dice)
    else:
        return 0
    
def calculate(dice, type):
    count = 0
    for i in dice:
        if i == type:
            count += i
    return count