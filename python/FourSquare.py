# -*- coding: utf-8 -*-
#
# Four-Square Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import Polybius, re

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
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = key.upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                key = key[1:]
            else:
                table[row][col] = alphabet[0]
            alphabet = alphabet.replace(table[row][col], '')
    return table


# 
# 加密
# 
def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        a, b = mangle(R, L, digraphs)
        ciphertext += a + b
    return ciphertext


def mangle(R, L, digraphs):
    a, b = digraphs[0], digraphs[1]
    a, b = position(table, a), position(table, b)
    return (R[a[0]][b[1]], L[b[0]][a[1]])


# 
# 解密
# 
def decrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        a, b = de_mangle(R, L, digraphs)
        ciphertext += a + b
    return ciphertext.lower()


def de_mangle(R, L, digraphs):
    a, b = digraphs[0], digraphs[1]
    a, b = position(R, a), position(L, b)
    return (table[a[0]][b[1]], table[b[0]][a[1]])


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


