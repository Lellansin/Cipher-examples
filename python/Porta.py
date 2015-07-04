# -*- coding: utf-8 -*-
#
# Porta Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# A与B相同，C与D相同，依次类推
alphabet = {
    "A":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]], "B":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]],
    "C":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["Z","N","O","P","Q","R","S","T","U","V","W","X","Y"]], "D":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Z","N","O","P","Q","R","S","T","U","V","W","X","Y"]],
    "E":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["Y","Z","N","O","P","Q","R","S","T","U","V","W","X"]], "F":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Y","Z","N","O","P","Q","R","S","T","U","V","W","X"]],
    "G":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["X","Y","Z","N","O","P","Q","R","S","T","U","V","W"]], "H":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["X","Y","Z","N","O","P","Q","R","S","T","U","V","W"]],
    "I":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["W","X","Y","Z","N","O","P","Q","R","S","T","U","V"]], "J":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["W","X","Y","Z","N","O","P","Q","R","S","T","U","V"]],
    "K":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["V","W","X","Y","Z","N","O","P","Q","R","S","T","U"]], "L":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["V","W","X","Y","Z","N","O","P","Q","R","S","T","U"]],
    "M":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["U","V","W","X","Y","Z","N","O","P","Q","R","S","T"]], "N":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["U","V","W","X","Y","Z","N","O","P","Q","R","S","T"]],
    "O":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["T","U","V","W","X","Y","Z","N","O","P","Q","R","S"]], "P":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["T","U","V","W","X","Y","Z","N","O","P","Q","R","S"]],
    "Q":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["S","T","U","V","W","X","Y","Z","N","O","P","Q","R"]], "R":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["S","T","U","V","W","X","Y","Z","N","O","P","Q","R"]],
    "S":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["R","S","T","U","V","W","X","Y","Z","N","O","P","Q"]], "T":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["R","S","T","U","V","W","X","Y","Z","N","O","P","Q"]],
    "U":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["Q","R","S","T","U","V","W","X","Y","Z","N","O","P"]], "V":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Q","R","S","T","U","V","W","X","Y","Z","N","O","P"]],
    "W":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["P","Q","R","S","T","U","V","W","X","Y","Z","N","O"]], "X":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["P","Q","R","S","T","U","V","W","X","Y","Z","N","O"]],
    "Y":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
         ["O","P","Q","R","S","T","U","V","W","X","Y","Z","N"]], "Z":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["O","P","Q","R","S","T","U","V","W","X","Y","Z","N"]]}

# 
# 生成密表
# 
def generateTable(key):
    table = []
    for ch in key.upper():
        table.append(alphabet[ch])
    return table

# 
# 加密
# 
def encrypt(key, words):
    cipher = ""
    count = 0
    table = generateTable(key)
    for ch in words.upper():
        cipher += getOpponent(table[count], ch)
        count = (count + 1) % len(table)
    return cipher

# 
# 解密
# 
def decrypt(key, words):
    return encrypt(key, words)

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
    row, col = getPosition(table, ch.upper())

    if row == 1:
        return table[0][col]
    elif row == 0:
        return table[1][col]
    else:
        return ch


if __name__ == "__main__":
    # 本例推算见 http://www.cryptool-online.org/index.php?option=com_content&view=article&id=124&Itemid=147&lang=en
    # 本算法类似 Kamasutra 升级版

    # 密匙
    key = "KEY"

    # 明文
    text = "GEHEIMNIS"

    # 加密字符串
    ciphertext = encrypt(key, text)

    # 密文
    print("密文:" + ciphertext)
    
    # 解密字符串
    print("原文:" + decrypt(key, ciphertext))
