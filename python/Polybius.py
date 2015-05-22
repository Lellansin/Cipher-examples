# -*- coding: utf-8 -*-
#
# Polybius Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import random

def rand(min, max):
    return int((max - min) * random.random() + min)

# 
# 随机生成棋盘
# 
def generate_table():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]

    for y in range(5):
        for x in range(5):
            table[x][y] = alphabet[rand(0, len(alphabet))]
            alphabet = alphabet.replace(table[x][y], '')
    return table

def getStr(x, format='%02s'):
    return ''.join(format % i for i in x)


# 
# 显示棋盘
# 
def print_table(table):
    print(' ' + getStr(range(1, 6)))
    for row in range(0, len(table)):
        print(str(row + 1) + getStr(table[row]))


# 
# 加密
# 
def encrypt(table, words):
    string = table
    cipher = ''

    for ch in words.upper():
        for row in range(len(table)):
            if ch in table[row]:
                x = str((table[row].index(ch) + 1))
                y = str(row + 1)
                cipher += y + x
    return cipher


# 
# 解密
# 
def decrypt(table, numbers):
    text = ''
    for index in range(0, len(numbers), 2):
        y = int(numbers[index]) - 1
        x = int(numbers[index + 1]) - 1
        text += table[y][x]
    return text


if __name__ == '__main__':
    # 随机生成棋盘
    table = generate_table()
    # 输出棋盘
    print_table(table)
    
    # 使用棋盘加密字符串
    ciphertext = encrypt(table, "hello, world")
    # 输出密文
    print(ciphertext)
    # 解密字符串
    print(decrypt(table, ciphertext))
