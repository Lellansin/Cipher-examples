# -*- coding: utf-8 -*-
#
# Transposition Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# 
# 置换
# 
def transposition(matrix, words):
    cipher = ''
    length = len(matrix)
    blanks = ''.join(' ' for i in range(length - 1))

    for x in range(0, len(words), length):
        # todo 优化
        item = words[ x : x + length ] + blanks
        for pos in matrix:
            cipher += item[pos - 1]

    return cipher.lower()


def reverse(matrix):
    length = len(matrix)
    arr = [0] * length
    for i in range(length):
        arr[matrix[i] - 1] = i + 1
    return arr


if __name__ == '__main__':
    # 本例推算见《密码学基础》(西安电子科技大学出版社) 第6页

    # 明文
    text = 'Informationsecurityisimportant';
    
    # 置换矩阵
    matrix = [2, 4, 1, 3]
    print('矩阵 ' + str(matrix))
    
    # 使用矩阵置换加密字符串
    ciphertext = transposition(matrix, text)

    # 输出密文
    print('密文 ' + ciphertext)

    # 置换矩阵反序即为密匙
    secret = reverse(matrix)
    print('密匙 ' + str(secret))

    # 解密字符串（使用密匙置换）
    print('解密 ' + transposition(secret, ciphertext))
