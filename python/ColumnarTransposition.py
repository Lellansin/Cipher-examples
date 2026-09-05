# -*- coding: utf-8 -*-
#
# Columnar Transposition Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 列置换密码: 明文按密钥长度逐行写入矩形, 依据密钥字母的字典序
# 依次自上而下读出各列得到密文
#

#
# 加密
#
def encrypt(key, words):
    key = key.upper()
    ncols = len(key)
    # 密钥字母按字典序排列后, 对应的列号顺序
    order = sorted(range(ncols), key=lambda col: key[col])

    ciphertext = ''
    for col in order:
        ciphertext += words[col::ncols]
    return ciphertext


#
# 解密: 按读出顺序切分密文, 放回矩形后按行读出
#
def decrypt(key, ciphertext):
    key = key.upper()
    ncols = len(key)
    order = sorted(range(ncols), key=lambda col: key[col])
    length = len(ciphertext)
    rows = (length + ncols - 1) // ncols

    # 每列实际字母数(末行不满时末尾几列少一个)
    counts = [len(range(col, length, ncols)) for col in range(ncols)]

    result = [''] * length
    idx = 0
    for col in order:
        for k, ch in enumerate(ciphertext[idx:idx + counts[col]]):
            result[col + k * ncols] = ch
        idx += counts[col]
    assert idx == length
    return ''.join(result)


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Columnar_transposition

    # 明文
    plaintext = 'this is wikipedia'

    # 密匙
    key = 'cipher'

    # 加密
    ciphertext = encrypt(key, plaintext.upper().replace(' ', ''))
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
