import math
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')


def load(file_name):
    grams = {}
    with open(os.path.join(DATA_DIR, file_name)) as f:
        total = 0
        for line in f:
            word, count = line.strip().split(' ')
            count = int(count)
            grams[word] = count
            total += count

    log_total = math.log(total)

    for w in grams:
        grams[w] = math.log(grams[w]) - log_total

    grams['*'] = 0 - log_total

    return grams

