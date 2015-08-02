
from itertools import combinations_with_replacement

from code.ngram_scorer import NGramScorer

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def _apply_key_letter(c, kl):
    a = ord(c) - 65
    b = ord(kl) - 65
    return chr(((a + b) % 26) + 65)


def _apply_key(text, key):
    new_text = ""
    for i in xrange(0, len(text)):
        new_text += _apply_key_letter(text[i], key[i % len(key)])
    return new_text


def crack(text, key_length):
    text = text.replace(' ', '')

    scorer = NGramScorer('english_quadgrams.txt')

    best_key = None
    best_score = -10**10
    best_text = None

    i = 0
    for current_key in combinations_with_replacement(ALPHABET, key_length):

        current_text = _apply_key(text, current_key)
        current_score = scorer.score(current_text)

        if current_score > best_score:
            best_score = current_score
            best_key = current_key
            best_text = current_text
            print i, best_key
        i += 1

    return best_text, best_key, best_score
