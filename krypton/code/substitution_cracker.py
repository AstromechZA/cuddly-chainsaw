import random
from collections import Counter

from code.ngram_scorer import NGramScorer

ALPHABET =        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_ORDERED = 'ETAOINSRHDLUCMFYWGPBVKXQJZ'

def _make_map(from_alphabet, to_alphabet):
    return {p[0]:p[1] for p in zip(from_alphabet, to_alphabet)}


def _shuffle_map(subject):
    k1, k2 = random.sample(subject.keys(), 2)
    t1 = subject[k1]
    t2 = subject[k2]
    subject[k1] = t2
    subject[k2] = t1
    return subject


def _build_cunning_map(text):
    counts = dict(Counter(text.replace(' ', '')))
    counts = sorted(counts.items(), key=lambda e: e[1])
    letters = ''.join(map(lambda e: e[0], counts))

    missing_letters = list(set(ALPHABET) - set(letters))
    letters = letters + ''.join(missing_letters)

    return _make_map(letters, ALPHABET_ORDERED)


def _apply_map(m, text):
    return ''.join(map(lambda l: m[l], text))


def crack(text, rounds=10000):
    text = text.replace(' ', '')

    scorer = NGramScorer('english_quadgrams.txt')

    best_map = _build_cunning_map(text)
    best_text = _apply_map(best_map, text)
    best_score = scorer.score(best_text)

    for x in xrange(1, rounds):

        current_map = _shuffle_map(best_map.copy())
        current_text = _apply_map(current_map, text)
        current_score = scorer.score(current_text)

        if current_score > best_score:
            best_score = current_score
            best_map = current_map
            best_text = current_text

    return best_text, best_map
