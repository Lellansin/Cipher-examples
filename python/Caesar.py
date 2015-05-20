# -*- coding: utf-8 -*-
#
# Caesar cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

def getShiftCh(ch, shift):
    if str.isalpha(str(ch)):
        asc = ord(ch) + shift;
        new_ch = asc
        if asc > ord('Z'):
            new_ch = (asc - ord('Z')) % 26 - 1 + ord('A')
        elif asc < ord('A'):
            new_ch = ord('Z') - ((ord('A') - asc) % 26 - 1)
        return unichr(new_ch)
    else:
        return ch

# 
# 凯撒密码
# 
def caesar(words, shift):
    cipher = ''
    for ch in words.upper():
        cipher += getShiftCh(ch, shift)
    return cipher.lower()

if __name__ == '__main__':
    text = 'hello world, this is Caesar cipher.'
    # 右移
    ciphertext = caesar(text, 3);
    print(ciphertext)
    # 左移
    print(caesar(ciphertext, -3))
