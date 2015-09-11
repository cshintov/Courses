"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
from time import time
# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

def timer(func):
    """timer decorator"""
    def timed(*args):
        """inner function"""
        start = time()
        result = func(*args)
        end = time()
        print func.__name__,'took',end-start,'seconds'
        return result
    return timed
    
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

def gen_histogram(sequence):
    """ makes a histogram of values from a sequence """
    histogram = {}
    for value in sequence:
        histogram[value] = histogram.get(value, 0) + 1
    return histogram


def score(hand):
    """ 
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    if len(hand) == 0:
        return 0
    elif len(hand) == 1:
        return hand[0]

    histogram = gen_histogram(hand)
    histogram = histogram.items()
    scores = map(lambda (value, occurrence): value * occurrence, histogram)

    return max(scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = xrange(1, num_die_sides+1)
    hands = gen_all_sequences(outcomes, num_free_dice)
    hands = [held_dice + hand for hand in hands]
    scores = [score(hand) for hand in hands]
    size = len(scores)
    score_distribution = gen_histogram(scores).items()
    term = lambda (score, okurens): score * okurens / float(size)
    exp_val = sum(map(term, score_distribution))

    return exp_val


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """ 
    ans = set([()])
    length = len(hand)
    if length  == 0:
        return ans
    if length <= 2:
        for dummy in range(length + 1):
            prefix = hand[:dummy]
            suffix = hand[dummy:]
            for die in suffix:
                hold = prefix + (die,)
                ans.add(hold)
    else:
        sub_holds = gen_all_holds(hand[1:])
        ans = set([(hand[0],) + hold for hold in sub_holds])
        ans = ans.union(sub_holds)
    return ans

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    length = len(hand)
    holds = gen_all_holds(hand)
    exval = lambda hold: expected_value(hold, num_die_sides, length - len(hold))
    exp_vals = [(exval(hold), hold) for hold in holds]
    exp_vals.sort(reverse=True)

    return exp_vals[0]

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

    hand = (4, 4, 4, 5, 5)
#    hand_score, hold = strategy(hand, num_die_sides)
    #print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
#run_example()


#import poc_testsuite
#poc_testsuite.run_suite(expected_value)
