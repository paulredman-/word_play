#!/usr/bin/python
"""
    First attempt.

    Show most common prefixes of length 2-5.

    (c) Paul Redman 2014
"""
import collections

from word_utils import get_word_list

word_list = get_word_list()

for length in range(2,6):
    prefix_counts = collections.defaultdict(int)

    for word in word_list:
        if len(word) >= length:
            prefix_counts[word[:length]] += 1

    # get the top 10 prefixes
    prefixes = sorted(prefix_counts.keys(), key = lambda k: prefix_counts[k], reverse = True)[:10]

    print("Length: %s" % length)
    #prefixes.sort()
    for prefix in prefixes:
        print("  %s %s" % (prefix, prefix_counts[prefix]))

