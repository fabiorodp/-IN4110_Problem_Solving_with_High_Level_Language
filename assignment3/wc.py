# Assignment 3 - IN4110 - H2020 - UiO
# Exercise 3.1
# Author: Fábio Rodrigues Pereira - fabior@uio.no

import sys, os
from pathlib import Path


def _counter(fn):
    """
    Function to count the number of lines, words and characters in a file.
    
    Paramters
    _____________________

    fn: string
        Name of the file that will be read.

    Return
    _____________________

    a:  int
        Number of lines.
    b:  int
        Number of words.
    c:  int
        Number of characters.
    fn: string
        path/File_name.
    """
    # Open the file
    file = open(fn, "rt")

    # Read the file
    data = file.read()

    # Get the informations needed
    a = sum(1 for line in open(fn))
    b = len(data.split())
    c = len(data)

    return a, b, c, fn


def wc(fn):
    """
    Function to print and return a nice list of words counts for all files in the current directory.

    or

    Function to print and return the count of lines, words and characters of a specific file.

    Paramters
    _____________________

    fn: string
        Path or file name or * (for all files) or *.py (for only python files).

    Return
    _____________________
    
    For multiple files:
        list_words: list of list
            List with lists of filename and it number of words.

    or for a specific file:
        a:  int
            Number of lines.
        b:  int
            Number of words.
        c:  int
            Number of characters.
        fn: string
            File name.
    """

    # Count lines, words and characters of multiple files
    if fn == "*":
        list_words = []
        for path in Path("").iterdir():
            if path.is_file():
                #print(path)
                a, b, c, fn = _counter(path)
                list_name_wordnr = [str(fn), b]
                list_words.append(list_name_wordnr)
        print(list_words)
        return list_words

    # Count lines, words and characters of multiple python files
    elif fn == "*.py":
        list_words = []
        for path in Path("").iterdir():
            if str(path)[-3:] == ".py":
                #print(path)
                a, b, c, fn = _counter(path)
                list_name_wordnr = [str(fn), b]
                list_words.append(list_name_wordnr)
        print(list_words)
        return list_words      

    # Count lines, words and characters of a specific file
    else:
        path = ""+fn
        a, b, c, fn = _counter(path)
        print(a, b, c, fn)
        return a, b, c, fn


if __name__ == "__main__":
    print("")
    print("Function with a specific file as argument:")
    os.system("touch text_file.txt")
    wc("text_file.txt")
    print("")
    print("")
    print("Function with all files as argument [[name, nr_words], ...]:")
    wc("*")
    print("")
    print("")
    print("Function with all python files as argument [[name, nr_words], ...]:")
    wc("*.py")
    print("")
