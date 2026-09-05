# -*- coding: utf-8 -*-
#
# Scytale Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 密码棒(天书)密码: 将明文按每行 n 个字母写成矩形(自左向右), 再逐列自上而下读出
# n 为密码棒每圈可容纳的字母数(即矩形宽度)
#

#
# 加密
#
def encrypt(words, n):
    if n < 2:
        return words
    return ''.join(words[col::n] for col in range(n))


#
# 解密: 按各列实际长度切分密文, 再放回矩形按行读出
#
def decrypt(ciphertext, n):
    if n < 2:
        return ciphertext
    length = len(ciphertext)
    rows = (length + n - 1) // n

    result = [''] * length
    idx = 0
    for col in range(n):
        # 第 col 列共有多少个字母
        count = (length - col + n - 1) // n
        for k, ch in enumerate(ciphertext[idx:idx + count]):
            result[col + k * n] = ch
        idx += count
    assert idx == length
    return ''.join(result)


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Scytale

    # 明文
    plaintext = 'meet us at the park today'

    # 每圈字母数
    n = 5

    # 加密
    ciphertext = encrypt(plaintext.upper().replace(' ', ''), n)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext, n))
