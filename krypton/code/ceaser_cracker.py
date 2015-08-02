
from code.ngram_scorer import NGramScorer

def _shift_c(c, distance):
    return chr((((ord(c) - 65) + distance) % 26) + 65)

def _shift(s, distance):
    return ''.join(map(lambda c: _shift_c(c, distance), s))

def crack(text):
    text = text.replace(' ', '')

    best_string = None
    best_score = -10**10

    scorer = NGramScorer('english_quadgrams.txt')

    for i in xrange(26):

        shifted_text = _shift(text, i)
        score = scorer.score(shifted_text)

        if score > best_score:
            best_score = score
            best_string = shifted_text

    return (best_string, best_score)
