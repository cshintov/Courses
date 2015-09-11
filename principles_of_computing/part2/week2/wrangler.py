"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"
codeskulptor.set_timeout(100)
# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    res = []
    previous = ""
    for item in list1:
        if item is not previous:
            res.append(item)
            previous = item
    return res


def binsearch(item, lista):
    """
    binary search of item in lista
    """
    mid = len(lista) / 2
    if mid == 0 :
        if item != lista[mid]:
            return False
    if item < lista[mid]:
        return binsearch(item, lista[:mid])
    if item > lista[mid]:
        return binsearch(item, lista[mid:])
    else :
        return True

def sel_list(lista, listb, comp):
    """
    select the list according to compare function
    """
    if comp(len(lista),len(listb)) == len(lista):
        return lista, listb
    else:
        return listb, lista

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    res = []
    min_list, max_list = sel_list(list1, list2, min)
    for item in min_list:
        if binsearch(item, max_list):
            res.append(item)
    return res


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    idxi = idxj = 0
    res = []
    while idxi < len(list1) and idxj < len(list2):
        if(list1[idxi] < list2[idxj]):
            res.append(list1[idxi])
            idxi += 1
        else:
            res.append(list2[idxj])
            idxj += 1
    if idxi < len(list1):
        res += list1[idxi:]
    if idxj < len(list2):
        res += list2[idxj:]
    return res

                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    mid = len(list1) / 2
    left = merge_sort(list1[:mid])
    right = merge_sort(list1[mid:])
    return merge(left, right)


#from test_suite import *
#run_suite(intersect)
# Function to generate all strings for the word wrangler game

def gen_strings(char, word):
    """
    generate all strings possible combining the character and the word
    """
    return [word[:idx] + char + word[idx:]for idx in range(len(word) + 1)]

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    result = [""]
    if len(word) is 0:
        return result
    if len(word) is 1:
        return result + [word]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    result = rest_strings[:]
    for string in rest_strings:
        result.extend(gen_strings(first, string))
    return result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = "http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt"
    return [word.strip() for word in urllib2.urlopen(url)]

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    

