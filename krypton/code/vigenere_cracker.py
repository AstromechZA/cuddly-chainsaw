
from itertools import combinations_with_replacement
from code.ngram_scorer import NGramScorer


def _shift_c(c, distance):
    return chr((((ord(c) - 65) + distance) % 26) + 65)

def _shift(s, distance):
    return ''.join(map(lambda c: _shift_c(c, distance), s))


def crack(text, key_length):
    text = text.replace(' ', '')
    text_length = len(text)
    sub_texts = [text[i::key_length] for i in xrange(0, key_length)]

    scorer = NGramScorer('english_monograms.txt')

    best_shifts = []
    best_texts = []
    best_scores = 0

    for sub_text in sub_texts:

        best_text = None
        best_score = -10**10
        best_shift = None

        for i in xrange(26):

            current_text = _shift(sub_text, i)
            current_score = scorer.score(current_text)

            if current_score > best_score:
                best_score = current_score
                best_text = current_text
                best_shift = i

        best_shifts.append(best_shift)
        best_texts.append(best_text)
        best_scores += best_score

    real_best_text = ""
    for i in xrange(0, text_length):
        real_best_text += best_texts[i % key_length][i / key_length]

    return real_best_text, best_shifts, best_scores

