#!/usr/bin/python3
from iofuncs import appendlines, cleartext, countlines, printlines, readfile
def findfunc(filename, command):
    """finds and runs operator for command token"""
    message = None
    if command == "log":
        message = input("Enter your message: ")
    operators = {
        'log': appendlines,
        'clear': cleartext,
        'length': countlines,
        'show': printlines,
        'print': readfile
    }
    if command in operators:
        if message:
            return operators[command](filename, message)
        return operators[command](filename)
