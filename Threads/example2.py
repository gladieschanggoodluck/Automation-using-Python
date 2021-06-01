## [File: example2.py]
## Concurrency - Example 
## Python version 3.X

## - Simple threads invoked to count words in files
## - Each thread counts words and reports the number of words
## - One thread for each provided file

# Add this list of books (text files) to the command line when running this Python Script: 
# BramStoker-Dracula.txt  mary1.txt shakespeare-hamlet.txt shakespeare-macbeth.txt
# (Note: space separated not comma separated!) 

import time
from threading import Thread
import sys

def wordCounter(filename):
    print("Counting words in: %s \n" % filename)
    time.sleep(5)
    # Count words in the file: 
    print("There are %d words in %s. \n" % (len(open(filename, "r+").read().split()), filename))


if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        # Thread targets the "wordCounter" function: wordCounter(sys.argv[i])
        t = Thread(target=wordCounter, args=(sys.argv[i],))
        t.start()
