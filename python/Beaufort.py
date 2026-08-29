# -*- coding: utf-8 -*-
#
# Beaufort Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 博福特密码: 密文 = 密匙 - 明文 (mod 26)
# 与维吉尼亚密码的 密文 = 明文 + 密匙 相反
# 是一个自反密码, 加密与解密是同一个操作
#
def beaufort(key, words):
    ciphertext = ''
    count = 0
    for ch in words:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[count % len(key)].upper()) - ord('A')
            ciphertext += chr((shift - (ord(ch) - base)) % 26 + base)
            count += 1
        else:
            ciphertext += ch
    return ciphertext

# 博福特密码加解密是同一个操作
decrypt = beaufort

if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

    # 明文
    plaintext = 'hello world, this is Beaufort cipher.'

    # 密匙
    key = 'key'

    # 加密
    ciphertext = beaufort(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
