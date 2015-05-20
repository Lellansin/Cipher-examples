# -*- coding: utf-8 -*-
#
# Caesar cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import re

A = ord('A')
Z = ord('Z')

def getAsc(asc):
    if asc > Z:
        return (asc - Z) % 26 - 1 + A
    elif asc < A:
        return Z - ((A - asc) % 26 - 1)
    else:
        return asc

def caesar(words, shift):
    cipher = ''
    for ch in re.compile(r'\W').sub('', words.upper()):
        cipher += str(unichr(getAsc(ord(ch) + shift)))
    return cipher.lower()

if __name__ == '__main__':
    text = 'hello world, this is Caesar cipher.'
    # text = 'abcdefghijklmnopqrstuvwxyz'

    # 右移
    ciphertext = caesar(text, 3);
    print(ciphertext)

    # 左移
    print(caesar(ciphertext, -3))
