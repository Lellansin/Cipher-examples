# -*- coding: utf-8 -*-
#
# Bifid Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import Polybius

# 
# 加密
# 
def encrypt(table, words):
    string = table
    cipher_row, cipher_col = '', ''

    for ch in words.upper():
        for row in range(len(table)):
            if ch in table[row]:
                cipher_row += str(row + 1)
                cipher_col += str((table[row].index(ch) + 1))
    return Polybius.decrypt(table, cipher_row + cipher_col)


# 
# 解密
# 
def decrypt(table, text):
    numbers = ''
    text = Polybius.encrypt(table, text)

    a, b = text[:len(text) / 2], text[len(text) / 2:]

    numbers = ''.join(a[i] + b[i] for i in range(len(a)))

    return Polybius.decrypt(table, numbers)


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Bifid_cipher

    # 初始化棋盘（也可以用 polybius.generate_table 来生成一个随机的)
    table = [['B', 'G', 'W', 'K', 'Z'],
             ['Q', 'P', 'N', 'D', 'S'],
             ['I', 'O', 'A', 'X', 'E'],
             ['F', 'C', 'L', 'U', 'M'],
             ['T', 'H', 'Y', 'V', 'R']]

    # 输出棋盘
    Polybius.print_table(table)

    # 密文
    text = "F L E E A T O N C E"
    
    # 使用棋盘加密字符串
    ciphertext = encrypt(table, text)

    # 密文
    print('密文: ' + ciphertext)

    # 解密字符串
    print('解密: ' + decrypt(table, ciphertext))
