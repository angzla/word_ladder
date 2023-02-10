#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if end_word not in dictionary_file or start_word not in dictionary_file:
        return None
    if len(start_word) != len(end_word):
        return None
    stack = []
    stack.append(start_word)
    deck = deque()
    deck.append(stack)
    while deck:
        curr_stack = deck.popleft()
        for word in dictionary_file:
            if _adjacent(word, curr_stack[0]) == True:
                if word == end_word:
                    final_word_ladder = curr_stack.append(word)
                    return (final_word_ladder)

                new_stack = curr_stack[:]
                new_stack.append(word)
                deck.append(new_stack)
                dictionary_file.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for x in range(len(ladder) - 1):
        if _adjacent(ladder[x], ladder[x + 1]) is False:
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    count = 0
    if len(word1) != len(word2):
        return False
    for x in range(len(word1)):
        if word1[x] != word2[x]:
            count += 1
    return count <= 1
