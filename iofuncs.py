#!/usr/bin/python3
"""module containing basic file io operations"""

def appendlines(filename='', message=''):
    """Adds lines to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(message + '\n')
        print('\nLogged!')

def cleartext(filename=''):
    """clears a file"""
    with open(filename, mode='w', encoding='utf-8') as a:
        a.write('')

def countlines(filename=''):
    """returns number of lines in the file"""
    linenum = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            linenum += 1
        print("This is the number of lines in my file: {}".format(linenum))

def printlines(filename=''):
    """prints lines with line numbers"""
    linenum = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            linenum += 1
            print("Line {}: {}".format(linenum, line), end='')

def readfile(filename=''):
    """prints the entire file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        print("My file: \n\n{}".format(f.read()), end='')

if __name__ ==  "__main__":
    doc = "test.txt"
    appendlines(doc, "hi")
    cleartext(doc)
    countlines(doc)
    printlines(doc)
    readfile(doc)
