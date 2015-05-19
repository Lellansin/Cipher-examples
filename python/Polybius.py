# -*- coding: utf-8 -*-
import re, random

def randomInt(min, max):
    return int((max - min) * random.random() + min)

# 
# 随机生成棋盘
# 
def generate_table():
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]

    for y in range(5):
        for x in range(5):
            table[x][y] = alphabet[randomInt(0, len(alphabet))]
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
def encode(table, words):
    string = table
    cipher = ''

    for ch in words.upper():
        for i in range(len(table)):
            if ch in table[i]:
                ox = str((table[i].index(ch) + 1))
                oy = str(i + 1)
                cipher += oy + ox
    return cipher

# 
# 解密
# 
def decode(table, numbers):
    text = ''
    for index in range(0, len(numbers), 2):
        oy = int(numbers[index]) - 1
        ox = int(numbers[index + 1]) - 1
        text += table[oy][ox]
    return text


if __name__ == '__main__':
    # 随机生成棋盘
    table = generate_table()
    # 输出棋盘
    print_table(table)
    
    # 使用棋盘加密字符串
    ciphertext = encode(table, "hello world")
    # 输出密文
    print(ciphertext)
    # 解密字符串
    print(decode(table, ciphertext))
