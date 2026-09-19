# -*- coding: utf-8 -*-
#
# ADFGX / ADFGVX Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
import re

#
# ADFGX/ADFGVX 密码: 两步加密
# 1) 分数化: 明文逐字符查 Polybius 方阵, 换成(行标,列标)两个字母
# 2) 置换: 分数化结果按置换密钥做列置换
# size=5 为 ADFGX (25 字母, I/J 合并), size=6 为 ADFGVX (36 字符, 含数字 0-9)
#
HEADERS = 'ADFGVX'


#
# 生成方阵: 密钥去重在前, 其余按序补齐; size=6 时在 A-J 首次出现后插入数字
# 返回 {字符: 行列字母对}, 如 {'A': 'AD', ...}
#
def generate_square(key='', size=6):
    mixed = ''
    for ch in re.sub(r'[^A-Za-z]', '', key).upper():
        if size == 5 and ch == 'J':
            ch = 'I'
        if ch not in mixed:
            mixed += ch
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if size == 5 else 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in alphabet:
        if ch not in mixed:
            mixed += ch
    if size == 6:
        for letter, digit in zip('ABCDEFGHIJ', '1234567890'):
            pos = mixed.index(letter) + 1
            mixed = mixed[:pos] + digit + mixed[pos:]

    square = {}
    headers = 'ADFGX' if size == 5 else 'ADFGVX'
    for i, ch in enumerate(mixed):
        square[ch] = headers[i // size] + headers[i % size]
    return square


#
# 列置换: 分数串按置换密钥逐行写入, 按密钥字母字典序整列读出
#
def columnar(text, trans_key, decrypt):
    trans_key = trans_key.upper()
    ncols = len(trans_key)
    order = sorted(range(ncols), key=lambda col: trans_key[col])
    length = len(text)

    if not decrypt:
        return ''.join(text[col::ncols] for col in order)

    rows = (length + ncols - 1) // ncols
    counts = [len(range(col, length, ncols)) for col in range(ncols)]
    result = [''] * length
    idx = 0
    for col in order:
        for k, ch in enumerate(text[idx:idx + counts[col]]):
            result[col + k * ncols] = ch
        idx += counts[col]
    return ''.join(result)


#
# 加密
#
def encrypt(square_key, trans_key, words, size=6):
    square = generate_square(square_key, size)
    if size == 5:
        chars = ['I' if c == 'J' else c for c in words.upper() if 'A' <= c <= 'Z']
    else:
        chars = [c for c in words.upper() if 'A' <= c <= 'Z' or '0' <= c <= '9']
    fractionated = ''.join(square[c] for c in chars)
    return columnar(fractionated, trans_key, False)


#
# 解密
#
def decrypt(square_key, trans_key, words, size=6):
    square = generate_square(square_key, size)
    inverse = dict((v, k) for k, v in square.items())
    fractionated = columnar(re.sub(r'[^ADFGVX]', '', words.upper()), trans_key, True)

    plaintext = ''
    for i in range(0, len(fractionated), 2):
        plaintext += inverse[fractionated[i:i+2]]
    return plaintext


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/ADFGVX_cipher
    # 密钥 nachtbommenwerper 恰好复现 wiki 示例的 6x6 方阵

    # 明文 (ADFGVX 支持数字)
    plaintext = 'attack at 1200am'

    # 方阵密匙与置换密匙
    square_key, trans_key = 'nachtbommenwerper', 'privacy'

    # 加密
    ciphertext = encrypt(square_key, trans_key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(square_key, trans_key, ciphertext))
