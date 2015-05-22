# -*- coding: utf-8 -*-
#
# Vigenere Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

ASC_A = ord('A')
TABLE_WIDTH = 26

# 
# 初始化密表
# 
def init_table():
    return [[chr((col + row) % TABLE_WIDTH + ASC_A) \
                     for col in range(TABLE_WIDTH)] \
                     for row in range(TABLE_WIDTH)]


# 
# 显示密表
# 
def print_table(table):
    output = ''
    for row in range(0, len(table)):
        for col in range(0, len(table[row])):
            output = output + table[row][col] + ' '
        output = output + '\n'
    print(output)


# 
# 加密
# 
def encrypt(table, key, words):
    cipher = ''
    count = 0
    key = key.upper()

    for ch in words.upper():
        if str.isalpha(str(ch)):
            key_shift  = ord(key[count % len(key)]) - ASC_A
            word_shift = ord(ch) - ASC_A
            cipher += table[key_shift][word_shift];
            count  += 1

    return cipher


# 
# 解密
# 
def decrypt(table, key, words):
    text = ''
    count = 0
    key = key.upper()
    for ch in words.upper():
        shift = ord(ch) - ord(key[count % len(key)])
        text += chr((shift + TABLE_WIDTH) % TABLE_WIDTH + ASC_A)
        count += 1
    return text.lower()


if __name__ == '__main__':
    # 本例推算见《密码学基础》(西安电子科技大学出版社) 第5页

    # 密匙
    secret = "computer";
    # 明文
    text = "block cipher design principles";

    # 初始化密表
    table = init_table()
    print_table(table)
    
    # 使用密表加密字符串
    ciphertext = encrypt(table, secret, text)
    # 输出密文
    print(ciphertext)
    # 解密字符串
    print(decrypt(table, secret, ciphertext))
