# -*- coding: utf-8 -*-
#
# Kamasutra Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# 
# 加密
# 
def encrypt(table, words):
    cipher = ''
    for ch in words:
        if str.isalpha(ch):
            ch = getOpponent(table, ch)
        cipher += ch
    return cipher

# 
# 解密
# 
def decrypt(table, words):
    return encrypt(table, words)

def toLower(ch, flag):
    if flag:
        return ch.lower()
    else:
        return ch

#
# 获取字母在密表中的位置
#
def getPosition(table, ch):
    row = -1
    
    if ch in table[0]:
        row = 0
    elif ch in table[1]:
        row = 1

    if row != -1:
        return (row, table[row].index(ch))
    else:
        return (None, None);

# 
# 根据位置获取对应另一个字母
# 
def getOpponent(table, ch):
    flag = False
    
    if ch.islower():
        flag = True

    row, col = getPosition(table, ch.upper())

    if row == 1:
        return toLower(table[0][col], flag)
    elif row == 0:
        return toLower(table[1][col], flag)
    else:
        return ch


if __name__ == '__main__':
    # 本例推算见 http://ruffnekk.stormloader.com/kamasutra_info.html

    # 密表就是密匙
    table = [
        [ 'K', 'B', 'J', 'H', 'O', 'E', 'S', 'N', 'W', 'Y', 'C', 'V', 'I' ],
        [ 'A', 'P', 'M', 'R', 'Z', 'Q', 'G', 'F', 'X', 'D', 'U', 'L', 'T' ] ]

    # 明文
    text = "This is an example";

    # 使用密表（同时也是密匙）加密字符串
    ciphertext = encrypt(table, text)

    # 密文
    print(ciphertext)
    
    # 解密字符串
    print(decrypt(table, ciphertext))
