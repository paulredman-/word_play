#!/usr/bin/python
"""
    Second version of analysis.

    Try to look for more traditional prefixes, by checking that the rest of the word, without the prefix, is also in the dictionary.
    Hence e.g. inter-view, inter-national, inter-play
    Note however that e.g. com-bustion and com-placent don't qualify under these rules.

    When displaying, give 3 examples so we can see what kind of words match.

    (c) Paul Redman 2014
"""
import collections

from word_utils import get_word_list

word_list = get_word_list()

word_store = {}

for word in word_list:
    word_store[word] = 1

for length in range(2,6):
    prefix_counts = collections.defaultdict(lambda : [int(), list()])

    for word in word_list:
        if len(word) >= length and word[length:] in word_store:
            prefix_counts[word[:length]][0] += 1
            prefix_counts[word[:length]][1].append(word)


    # get the top 10 prefixes
    prefixes = sorted(prefix_counts.keys(), key = lambda k: prefix_counts[k], reverse = True)[:10]

    print("Length: %s" % length)
    #prefixes.sort()
    for prefix in prefixes:
        print("  %s %s %s" % (prefix, prefix_counts[prefix][0], str(prefix_counts[prefix][1][:3])))

