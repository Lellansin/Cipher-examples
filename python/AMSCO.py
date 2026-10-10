# -*- coding: utf-8 -*-
#
# AMSCO Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# AMSCO 密码 (ACA): 列置换的变体
# 明文按行填入网格, 单元格交替容纳 1 或 2 个字母
# (首格 1 个, 按 行号+列号 的奇偶交替), 再按密钥字母序整列读出
#

#
# 生成交替尺寸的索引网格: [行][列] -> 明文位置索引列表
#
def _grid(length, ncols):
    rows, p, r = [], 0, 0
    while p < length:
        row = []
        for c in range(ncols):
            size = 1 if (r + c) % 2 == 0 else 2
            row.append(list(range(p, min(p + size, length))))
            p += size
        while len(row) < ncols:
            row.append([])
        rows.append(row)
        r += 1
    return rows


#
# 加密
#
def encrypt(key, words):
    order = sorted(range(len(key)), key=lambda c: key[c].upper())
    rows = _grid(len(words), len(key))
    ciphertext = ''
    for col in order:
        for row in rows:
            ciphertext += ''.join(words[i] for i in row[col])
    return ciphertext.upper()


#
# 解密
#
def decrypt(key, words):
    order = sorted(range(len(key)), key=lambda c: key[c].upper())
    rows = _grid(len(words), len(key))
    result = [''] * len(words)
    p = 0
    for col in order:
        for row in rows:
            for i in row[col]:
                result[i] = words[p]
                p += 1
    return ''.join(result)


if __name__ == '__main__':
    # AMSCO 规则见 American Cryptogram Association
    # 手工推算: ABCD / 密钥 CAT -> BCAD (首格 1 字母, 次格 2 字母交替)

    # 明文
    plaintext = 'hello world'

    # 密匙
    key = 'cat'

    # 加密
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
