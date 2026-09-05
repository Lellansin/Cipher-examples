# -*- coding: utf-8 -*-
#
# Keyed Caesar Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 带密钥的凯撒密码: 先用密钥单词生成混合字母表(密钥去重在前, 其余字母按序补齐),
# 明文字母在标准字母表中的序号 i 映射为混合字母表序号 (i + shift) mod 26 处的字母
#

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#
# 生成混合字母表
#
def generate_alphabet(key, shift):
    # 密钥去重, 保留首次出现
    mixed = ''
    for ch in key.upper():
        if ch.isalpha() and ch not in mixed:
            mixed += ch
    # 其余字母按序补齐
    for ch in ALPHABET:
        if ch not in mixed:
            mixed += ch
    shift %= len(ALPHABET)
    return mixed[shift:] + mixed[:shift]


#
# 加密
#
def encrypt(key, shift, words):
    mixed = generate_alphabet(key, shift)
    ciphertext = ''
    for ch in words:
        if 'a' <= ch <= 'z':
            ciphertext += mixed[ALPHABET.index(ch.upper())].lower()
        elif 'A' <= ch <= 'Z':
            ciphertext += mixed[ALPHABET.index(ch)]
        else:
            ciphertext += ch
    return ciphertext


#
# 解密
#
def decrypt(key, shift, words):
    mixed = generate_alphabet(key, shift)
    plaintext = ''
    for ch in words:
        upper = ch.upper()
        if 'A' <= upper <= 'Z' and upper in mixed:
            plain = ALPHABET[mixed.index(upper)]
            plaintext += plain.lower() if ch.islower() else plain
        else:
            plaintext += ch
    return plaintext


if __name__ == '__main__':
    # 混合字母表构造见 http://en.wikipedia.org/wiki/Keyword_cipher

    # 明文
    plaintext = 'hello world, this is keyed caesar.'

    # 密匙单词与位移
    key, shift = 'zebra', 1

    # 加密
    ciphertext = encrypt(key, shift, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, shift, ciphertext))
