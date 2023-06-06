#!/usr/bin/python3
def uppercase(string):
    uppercase_string = ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in string)
    print(uppercase_string)
