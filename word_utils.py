"""
    Common routines for analysing words

    (c) Paul Redman 2014
"""

import os
import sys

import urllib2
import zipfile

# make sure we are in the script dir
sdir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(sdir)

def get_url(url):
    """ return the contents of a URL """
    urlh = urllib2.urlopen(url)
    txt = urlh.read()
    urlh.close()

    return txt


def read_file(fname):
    """ return the contents of a file """
    ifh = open(fname, "rb")
    txt = ifh.read()
    ifh.close()

    return txt


def write_file(fname, txt):
    """ write out the txt to a file.  Existing file contents will be lost """
    ofh = open(fname, "wb")
    ofh.write(txt)
    ofh.close()


def get_word_list():
    # get the word file.  Cache it if not there, use cache if there
    cache_file = "wlist_match8.zip"
    if not os.path.isfile(cache_file):
        print("Downloading word list - no cached version")
        data = get_url("http://www.keithv.com/software/wlist/wlist_match8.zip")
        write_file(cache_file, data)

    ziph = zipfile.ZipFile(cache_file)
    txt = ziph.read("wlist_match8.txt")
    ziph.close()

    return txt.splitlines()


