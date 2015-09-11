
def gen_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                pos = outcomes.index(item)
                new = outcomes[:pos]+outcomes[pos+1:]
                for newitem in new:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans

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

import poc_holds_testsuite as test
test.run_suite(gen_all_holds)
