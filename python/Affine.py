# -*- coding: utf-8 -*-
#
# Affine cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

WIDTH = 26       # 密表宽度
ASC_A = ord('A') # 密表起点 (使用字母表做密表)

# 
# 加密
# 
def encrypt(key, words):
    return ''.join([shift(key, ch) for ch in words.upper()])

# 
# 解密
# 
def decrypt(key, words):
    a, b = modInverse(key[0], WIDTH), -key[1]
    return ''.join([unshift([a, b], ch) for ch in words.upper()])

# 
# E(x) = (ax + b) mod m
#
def shift(key, ch):
    if str.isalpha(ch):
        offset = ord(ch) - ASC_A
        return chr(((key[0] * offset + key[1]) % WIDTH) + ASC_A)
    return ''

# 
# D(x) = a^{-1}(x - b) mod m
# 
def unshift(key, ch):
    offset = ord(ch) - ASC_A
    return chr(((key[0] * (offset + key[1])) % WIDTH) + ASC_A)

# 
# 判断 a 与 b 是否互素 (Euclid's Algorithm)
# 
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# 
# 求 a 在密表中的乘法逆
# 
def modInverse(a, m):
    if gcd(a, m) != 1:
        print("Error: a 与 m 不互素")
        quit()
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Affine_cipher
    
    # 明文
    text = 'AFFINECIPHER'
    # 密匙
    key = [5, 8]
    # 加密
    ciphertext = encrypt(key, text)
    # 密文
    print (ciphertext)
    # 解密
    print (decrypt(key, ciphertext))
