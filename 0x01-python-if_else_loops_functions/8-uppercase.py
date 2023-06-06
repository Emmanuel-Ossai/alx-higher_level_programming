#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            ch = chr(ord(ch) - 32)
        uppercase_str += ch

    print(uppercase_str)
