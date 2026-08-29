# -*- coding: utf-8 -*-
#
# Railfence Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 栅栏密码: 将明文沿 W 形(之字形)的栅栏逐个书写, 再按栏拼接成密文
#

#
# 加密
#
def encrypt(words, rails):
    if rails < 2:
        return words
    fence = [[] for row in range(rails)]
    rail, step = 0, 1
    for ch in words:
        fence[rail].append(ch)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step
    return ''.join(''.join(row) for row in fence)


#
# 解密: 先重建之字形轨迹, 按各栏长度切分密文, 再沿轨迹取回
#
def decrypt(ciphertext, rails):
    if rails < 2:
        return ciphertext
    pattern = []
    rail, step = 0, 1
    for i in range(len(ciphertext)):
        pattern.append(rail)
        if rail == 0:
            step = 1
        elif rail == rails - 1:
            step = -1
        rail += step

    rows, idx = [], 0
    for row in range(rails):
        num = pattern.count(row)
        rows.append(list(ciphertext[idx:idx + num]))
        idx += num

    plaintext = ''
    for row in pattern:
        plaintext += rows[row].pop(0)
    return plaintext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Rail_fence_cipher

    # 明文
    plaintext = 'WEAREDISCOVEREDFLEEATONCE'

    # 栏数
    rails = 3

    # 加密
    ciphertext = encrypt(plaintext, rails)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext, rails))
