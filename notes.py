#!/usr/bin/python3
import findfunc as look
"""
Methods:
    appendlines(filename, message)
    cleartext(filename)
    countlines(filename)
    printlines(filename)
    readfile(filename)
"""
if __name__ == "__main__":
    # first command is file name, second command is the operator, third is the
    # message
    try:
        while True:
            command = input(
                "\nNotebook Options:\n\n[log]: Add note\n[print]: Print entries\n[show]: Show line numbers\n[length]: Print length\n[clear]: Clear notes\n[quit]: <ctrl> + c\n\n-----> ")
            doc = 'journal.txt'
            look.findfunc(doc, command)
    except KeyboardInterrupt:
        print("\nGoodbye.")
