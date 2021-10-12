import random
from typing import List


def init(count: int = 20, min_length: int = 6) -> (List, List):
    # NOTE: As tempting as it may be, you are not allowed to modify/debug anything in this section
    #       so that means no print statements or other ways to just find the words before they are scrambled.
    #       treat this section as a black box.

    f = open('wordlist.txt', 'r')
    words = f.read().splitlines()
    scrambled = []

    candidate_words = []
    for word in words:
        if len(word) >= min_length:
            candidate_words.append(word)
    candidate_count = len(candidate_words)

    for i in range(0, count):
        idx = random.randint(0, candidate_count)
        word = candidate_words[idx]
        chars = list(word)
        random.shuffle(chars)
        scrambled.append(''.join(chars))

    return words, scrambled
