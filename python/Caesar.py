# -*- coding: utf-8 -*-
#
# Caesar cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

a, z = ord('a'), ord('z')
A, Z = ord('A'), ord('Z')

# 
# 凯撒密码
# 
def caesar(words, shift):
    cipher = ''

    for ch in words:
        if ch.islower():
            cipher += getShiftCh(ch, a, z, shift)
        elif ch.isupper():
            cipher += getShiftCh(ch, A, Z, shift)
        else:
            cipher += ch
    return cipher


def getShiftCh(ch, A, Z, shift):
    result = dif = ord(ch) + shift
    if dif > Z:
        result = (dif - Z) % 26 - 1 + A
    elif dif < A:
        result = Z - ((A - dif) % 26 - 1)
    return chr(result)


if __name__ == '__main__':
    text = 'hello world, this is Caesar cipher.'
    
    # 右移
    ciphertext = caesar(text, 3);
    print(ciphertext)

    # 左移
    print(caesar(ciphertext, -3))
