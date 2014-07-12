#!/usr/bin/python
"""
   Identify proper nouns in a text (Persuasion by Jane Austen)

   Do this by looking for words that are always capitalized.  Note that all upper-cased is fine as well

   We want to avoid the beginning of sentences.  But more complicated as abbreviations also end in .

   So look for words that are always capitalized.

   Seems to produce reasonable results - cf http://en.wikipedia.org/wiki/Persuasion_(novel)?section=1#Plot_introduction
   But also produces months, days of week, titles (Mr., Dr.) and a few words that appears just once at the start of a sentence (Doubtless, Whoever).

   (c) Paul Redman 2014
"""

import re

try:
    import cjson
except ImportError:
    print("cjson not available")

from word_utils import cache_url, read_file, extract_one_between_tags, write_file

cache_url("http://www.gutenberg.org/cache/epub/105/pg105.txt", "persuasion.txt")
txt = read_file("persuasion.txt")

txt = extract_one_between_tags(txt, "*** START OF THIS PROJECT GUTENBERG EBOOK PERSUASION ***", "*** END OF THIS PROJECT GUTENBERG EBOOK PERSUASION ***")
pos = txt.find("Persuasion")  # cut out a Gutenberg credit
txt = txt[pos:]
pos = txt.find("Finis")  # cut out a Gutenberg credit
txt = txt[:pos + 6]

words = txt.split()

# the key is the lower case word
# the value is a tuple of (the first capitalization, whether always capitalized the same, the count (any capitalization)
word_store = {}

cre_keep_chars = re.compile(r"[A-Za-z\-]*")
word_count = 0

for word in words:
    word_count += 1
    word = cre_keep_chars.findall(word)[0].rstrip("-")  # hyphens are fine, but not at the end
    if word == "":
        continue
    word_lc = word.lower()
    if word_lc not in word_store:
        # need to use a list so we can update it
        word_store[word_lc] = [word, word[0].isupper(), 1]
    else:
        word_store[word_lc][2] += 1
        if word.islower():
            # sometimes lower-cased
            word_store[word_lc][1] = False

print("Word count = %s" % word_count)
print("Distinct word count = %s" % len(word_store.keys()))

words = word_store.keys()
# take out words that appear in lower-case
words = filter(lambda word: word_store[word][1], words)
print("Upper-cased (at least once) word count = %s" % len(words))
# take out words that aren't capitalized
words = filter(lambda word: word_store[word][0][0].isupper(), words)
# take out "I" - this is always capitalized, but not a proper name
if "i" in words:
    words.remove("i")
print("Potential proper names count = %s" % len(words))

proper_noun_store = {}  # from proper noun to count
for word in words:
    proper_noun_store[word_store[word][0]] = word_store[word][2]

try:
    json_txt = cjson.encode(proper_noun_store)
except:
    # we've already reported cjson missing
    json_txt = None
    pass

if json_txt is not None:
    write_file("persuasion_proper_nouns.json", json_txt)

words.sort(key = lambda word: word_store[word][2], reverse = True)
words = words[:40]
for word in words:
    print("%5s %s" % (word_store[word][2], word_store[word][0]))