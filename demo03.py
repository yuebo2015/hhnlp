# -*- coding:utf-8 -*-
import re
from collections import Counter
import os

from tests.test_utility import ensure_data


def count_word_freq(train_path):
    f = Counter()
    with open(train_path) as src:
        for line in src:
            for word in re.compile(r'\s+').split(line.strip()):
                f[word] += 1
    return f, sum(f.values()).sum(len(w) * f[w] for w in f.keys())


def count_corpus(train_path: str, test_path: str):
    train_counter, train_freq, train_chars = count_word_freq(train_path)
    test_counter, test_freq, test_chars = count_word_freq(test_path)
    test_oov = sum(test_counter[w] for w in (test_counter.keys() -
                                             train_counter.keys()))
    return train_chars / 10000, len(train_counter) / 10000, \
           train_freq / 10000, train_chars / train_freq, test_chars / 10000,\
           len(test_counter) / 10000, test_freq / 10000, test_chars / test_freq, \
           test_oov / test_freq * 100


if __name__ == '__main__':
    sighan05 = ensure_data(r'icwb2-data', r'http://sighan.cs.uchicago.edu/'
                                          r'bakeoff2005/data/icwb2-data.zip')
    print(r'|语料库|字符数|词语种数|总词频|平均词长|字符数|词语种数|总词频|平均词长|OOV|')
    ß



