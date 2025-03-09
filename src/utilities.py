import random
import math


def argmaxall(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
     argmaxall returns a list of all of the elements with maximal value."""
    maxv = -math.inf  # negative infinity
    axvals = []  # list of maximal elements
    for (e, v) in gen:
        if v > maxv:
            maxvals, maxv = [e], v
        elif v == maxv:
            maxvals.append(e)
    return maxvals


def argmaxe(gen):
    """gen is a generator of (element,value) pairs, where value is a real.
    argmaxe returns an element with maximal value.
    If there are multiple elements with the max value, one is returned at random."""
    return random.choice(argmaxall(gen))


def argmax(lst):
    """returns maximum index in a list"""
    return argmaxe(enumerate(lst))
# Try:
# argmax([1,6,3,77,3,55,23])


def argmaxd(dct):
    """returns the arg max of a dictionary dct"""
    return argmaxe(dct.items())
# Try:
# arxmaxd({2:5, 5:9, 7:7})


def flip(prob):
    """returns true with probability prob"""
    return random.random() < prob


def select_from_dist(item_prob_dist):
    """ returns a value from a distribution.
    item_prob_dist is an item:probability disctionary, where the probabilities sum to 1.
    returns an item chosen in proportion to its probability"""
    ranreal = random.random()
    for (it, prob) in item_prob_dist.items():
        if ranreal < prob:
            return it
        else:
            ranreal -= prob
    raise RuntimeError(f"{item_prob_dist} is not a probability distribution")