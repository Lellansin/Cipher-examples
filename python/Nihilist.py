# -*- coding: utf-8 -*-
#
# Nihilist Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 虚无主义密码: 明文与密钥都先经 Polybius 方阵转成两位数
# 密文 = 明文数 + 密钥数 (普通加法, 不取模, 可能出现三位数)
#

#
# 生成棋盘 (25 字母, 无 J)
#
def generate_square(key=''):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    mixed = ''
    for ch in key.upper():
        if ch in alphabet and ch not in mixed:
            mixed += ch
    for ch in alphabet:
        if ch not in mixed:
            mixed += ch
    square = {}
    for i, ch in enumerate(mixed):
        square[ch] = (i // 5 + 1, i % 5 + 1)
    return square


#
# 加密
#
def encrypt(square_key, key, words):
    square = generate_square(square_key)
    key = [ch for ch in key.upper() if ch in square]
    if not key or not words.strip():
        raise ValueError('明文与密钥不能为空')

    numbers = []
    count = 0
    for ch in words.upper():
        if ch in square:
            pr, pc = square[ch]
            kr, kc = square[key[count % len(key)]]
            numbers.append((pr * 10 + pc) + (kr * 10 + kc))
            count += 1
    return ' '.join(str(n) for n in numbers)


#
# 解密
#
def decrypt(square_key, key, text):
    square = generate_square(square_key)
    reverse = dict((v, k) for k, v in square.items())
    key = [ch for ch in key.upper() if ch in square]
    numbers = [int(n) for n in text.split()]
    if not key or not numbers:
        raise ValueError('密文与密钥不能为空')

    plaintext = ''
    for count, number in enumerate(numbers):
        kr, kc = square[key[count % len(key)]]
        pair = number - (kr * 10 + kc)
        plaintext += reverse[(pair // 10, pair % 10)]
    return plaintext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Nihilist_cipher

    # 明文
    plaintext = 'dynamite winter palace'

    # 棋盘密匙与密钥
    square_key, key = 'zebras', 'russian'

    # 加密
    ciphertext = encrypt(square_key, key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(square_key, key, ciphertext))
