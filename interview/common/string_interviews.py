"""
This module includes all the interview functions about strings.
"""


def is_isomorphic(word_1: str, word_2: str):
    """
    Example:
    Input: s = "egg", t = "add"
    Output: true
    @param word_1: <str> word 1
    @param word_2: <str> word 2
    @return: <bool> whether two words are isomorphic
    """
    return len(set(word_1)) == len(set(word_2)) == len(set(zip(word_1, word_2)))
