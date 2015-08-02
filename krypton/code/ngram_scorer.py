
import data_loader

class NGramScorer(object):

    def __init__(self, grams_file):
        self.data = data_loader.load(grams_file)

        tk = self.data.keys()[1] if self.data.keys()[0] == '*' else self.data.keys()[0]
        self.gram_size = len(tk)

    def score(self, text):
        text = text.replace(' ', '')
        total_score = 0
        for n_gram in get_ngrams(self.gram_size, text):
            total_score += self.data.get(n_gram, self.data['*'])
        return total_score

def get_ngrams(l, text):
    for i in xrange(0,len(text)-l):
        yield text[i:i+l]
