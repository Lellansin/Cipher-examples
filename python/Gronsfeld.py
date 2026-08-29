# -*- coding: utf-8 -*-
#
# Gronsfeld Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 格朗斯菲尔德密码: 与维吉尼亚密码相同, 只是密匙为数字 0-9
# 数字密匙 0123 等价于维吉尼亚密匙 ABCD
#

#
# 加密
#
def encrypt(key, words):
    ciphertext = ''
    count = 0
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = int(key[count % len(key)])
            ciphertext += chr((ord(ch) - base + shift) % 26 + base)
            count += 1
        else:
            ciphertext += ch
    return ciphertext


#
# 解密
#
def decrypt(key, words):
    ciphertext = ''
    count = 0
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = int(key[count % len(key)])
            ciphertext += chr((ord(ch) - base - shift) % 26 + base)
            count += 1
        else:
            ciphertext += ch
    return ciphertext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    # 即维吉尼亚密匙 ABCD 的例子, 等价于格朗斯菲尔德密匙 0123

    # 明文
    plaintext = 'crypto is short for cryptography'

    # 密匙
    key = '0123'

    # 加密
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
