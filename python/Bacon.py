# -*- coding: utf-8 -*-
#
# Bacon's cipher
# 
# @author  Lukasz Banasiak <lukasz@banasiak.me>
# @website https://github.com/lukaszbanasiak/python-ciphers/blob/master/Bacon.py
#
from unicodedata import normalize
import re

def generate_dict():

    """
    Create Bacon dictionary.

    a   AAAAA   g     AABBA   n    ABBAA   t     BAABA
    b   AAAAB   h     AABBB   o    ABBAB   u-v   BAABB
    c   AAABA   i-j   ABAAA   p    ABBBA   w     BABAA
    d   AAABB   k     ABAAB   q    ABBBB   x     BABAB
    e   AABAA   l     ABABA   r    BAAAA   y     BABBA
    f   AABAB   m     ABABB   s    BAAAB   z     BABBB

    :return: Bacon dict
    """

    bacon_dict = {}

    for i in xrange(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        bacon_dict[tmp] = chr(65 + i)

    return bacon_dict


def encode(words, bacon_dict):

    """
    Encrypt text to Bacon's cipher.

    :param words: string to encrypt
    :param bacon_dict: Bacon dict
    :return: encrypted string
    """

    cipher = ''
    bacon_dict = {v: k for k, v in bacon_dict.items()}  # hack to get key from value - reverse dict
    words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents
    words = words.upper()
    words = re.sub(r'[^A-Z]+', '', words)

    for i in words:
            cipher += bacon_dict.get(i).upper()
    return cipher


def decode(words, bacon_dict):

    """
    Decrypt Bacon's cipher to text.

    :param words: string to decrypt
    :param bacon_dict: Bacon dict
    :return: decrypted string
    """

    cipher = ''
    words = words.lower()
    words = re.sub(r'[^ab]+', '', words)

    for i in xrange(0, len(words) / 5):
        cipher += bacon_dict.get(words[i * 5:i * 5 + 5], ' ')
    return cipher


if __name__ == '__main__':
    text = u'hello world'
    bacon_dict = generate_dict()
    print(bacon_dict)
    ciphertext = encode(text, bacon_dict)

    print('encode: ' + ciphertext)
    print('decode: ' + decode(ciphertext, bacon_dict))
