# -*- coding: utf-8 -*-
#
# Two-Square Cipher (vertical)
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
# 二方密码: 两个 5x5 棋盘上下排列 (vertical), 明文按两两一组
# 前一个字母在上棋盘查找, 后一个字母在下棋盘查找
# 不同列时, 以对方的列与自己的行交叉取字母 (矩形对角)
# 同列时交叉点就是原字母, 因此密文与明文相同 (transparency)
# 加密与解密是同一个操作
#
import re

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

# todo
def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return (row, col)
    return (None, None)

# 
# 加密
# 
def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[^A-Za-z]', '', words).upper().replace('Q', '')
    up, down = generate_table(keys[0]), generate_table(keys[1])

    for i in range(0, len(words), 2):
        digraph = words[i:i+2]
        ciphertext += mangle(up, down, digraph)
    return ciphertext

def mangle(up, down, digraph):
    # 奇数长度的末尾单字原样保留
    if len(digraph) < 2:
        return digraph
    a, b = position(up, digraph[0]), position(down, digraph[1])
    # 棋盘外字符原样保留
    if a[0] is None or b[0] is None:
        return digraph
    # 以对方的列与自己的行交叉取字母
    return up[a[0]][b[1]] + down[b[0]][a[1]]

# 二方密码加解密是同一个操作
decrypt = encrypt

if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Two-square_cipher

    # 明文
    plaintext = 'help me obiwankenobi'

    # 密匙
    keys = ['example', 'keyword']

    # 加密
    ciphertext = encrypt(keys, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(keys, ciphertext))
