# -*- coding: utf-8 -*-
#
# Chaocipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 查奥密码 (Byrne, 1918): 左(密文)右(明文)两个字母盘, 索引 0 为天顶, 13 为天底
# 每加密一个字母:
# 1) 在右盘找到明文字母所在索引, 取左盘同索引字母作为密文
# 2) 置换左盘: 取出索引 25 (zenith-1) 的字母, 索引 24..13 顺时针移一格,
#    取出的字母放回天底 (索引 13)
# 3) 置换右盘: 先逆时针转一格 (天顶字母移到索引 25), 取出索引 2 (zenith+2)
#    的字母, 索引 3..13 逆时针移一格, 取出的字母放回天底
# 解密仅在步骤 1 反向 (在左盘找密文字母、读右盘), 置换过程完全相同
#
# 算法规则见 http://en.wikipedia.org/wiki/Chaocipher
#

#
# 置换左盘
#
def permute_left(disk):
    return disk[:13] + [disk[25]] + disk[13:25]


#
# 置换右盘
#
def permute_right(disk):
    disk = disk[1:] + disk[:1]          # 逆时针转一格
    return disk[:2] + disk[3:14] + [disk[2]] + disk[14:]


#
# 初始化状态 (密钥为两个 26 字母表: 去重在前, 其余按序补齐)
#
def create(left='', right=''):
    def keyed(key):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        mixed = ''
        for ch in key.upper():
            if ch in alphabet and ch not in mixed:
                mixed += ch
        for ch in alphabet:
            if ch not in mixed:
                mixed += ch
        return [ch for ch in mixed]
    return {'left': keyed(left), 'right': keyed(right)}


#
# 加密
#
def encrypt(state, words):
    result = ''
    for ch in words.upper():
        if 'A' <= ch <= 'Z':
            idx = state['right'].index(ch)
            result += state['left'][idx]
            state['left'] = permute_left(state['left'])
            state['right'] = permute_right(state['right'])
    return result


#
# 解密 (在左盘查密文字母、读右盘)
#
def decrypt(state, words):
    result = ''
    for ch in words.upper():
        if 'A' <= ch <= 'Z':
            idx = state['left'].index(ch)
            result += state['right'][idx]
            state['left'] = permute_left(state['left'])
            state['right'] = permute_right(state['right'])
    return result


if __name__ == '__main__':
    # 算法规则见 http://en.wikipedia.org/wiki/Chaocipher

    # 密匙 (左右盘字母表)
    state = create(left='swift', right='crypton')

    # 明文
    plaintext = 'the quick brown fox jumps over the lazy dog'

    # 加密
    ciphertext = encrypt(state, plaintext)
    print(ciphertext)

    # 解密 (重置状态)
    state = create(left='swift', right='crypton')
    print(decrypt(state, ciphertext))
