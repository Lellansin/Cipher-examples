# -*- coding: utf-8 -*-
#
# Four-Square Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import re

# 默认密表
table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 

# 
# 生成棋盘
# 
def generate_table(key = ''):
    # wiki原文：usually omitting "Q" or putting both "I" and "J" in the same location to reduce the alphabet to fit
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '')
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table

# 
# 加密
# 
def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L  = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += mangle(R, L, digraphs)
    return ciphertext


def mangle(R, L, digraphs):
    a = position(table, digraphs[0])
    b = position(table, digraphs[1])
    return R[a[0]][b[1]] + L[b[0]][a[1]]

# 
# 解密
# 
def decrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += unmangle(R, L, digraphs)
    return ciphertext.lower()

def unmangle(R, L, digraphs):
    a = position(R, digraphs[0])
    b = position(L, digraphs[1])
    return table[a[0]][b[1]] + table[b[0]][a[1]]

# todo
def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return (row, col)
    return (None, None)


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Four-square_cipher

    # 明文
    plaintext = 'help me obiwankenobi'

    # 密匙
    key = ['example', 'keyword']

    # 加密
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
