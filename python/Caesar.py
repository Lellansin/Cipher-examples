# -*- coding: utf-8 -*-
#
# Caesar cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#


def caesar(words, shift):
    cipher = ''
    for ch in words.lower():
        cipher += getShiftCh(ch, shift)
    return cipher


def getShiftCh(ch, shift):
    if str.isalpha(str(ch)):
        A, Z = ord('a'), ord('z')
        result = dif = ord(ch) + shift
        if dif > Z:
            result = (dif - Z) % 26 - 1 + A
        elif dif < A:
            result = Z - ((A - dif) % 26 - 1)
        return unichr(result)
    else:
        return ch


if __name__ == '__main__':
    text = 'hello world, this is Caesar cipher.'
    
    # 右移
    ciphertext = caesar(text, 3);
    print(ciphertext)

    # 左移
    print(caesar(ciphertext, -3))
