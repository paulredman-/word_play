#!/usr/bin/python
"""
    Show the frequency of word-lengths.
    It turns out that - on this word list - 7 is the most common length.

    (c) Paul Redman 2014
"""
import collections

from word_utils import get_word_list

word_list = get_word_list()

length_counts = collections.defaultdict(int)

for word in word_list:
    length_counts[len(word)] += 1

lengths = sorted(length_counts.keys())

for length in lengths:
    print("  %s %s" % (length, length_counts[length]))

