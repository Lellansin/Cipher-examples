# -*- coding: utf-8 -*-
#
# Navajo Code
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 纳瓦霍密码 (二战美军陆战队 Code Talkers): 严格说是一种代码而非密码
# 每个拉丁字母用对应的纳瓦霍语单词拼读, 如 A = WOL-LA-CHEE (蚂蚁)
# 代码表为美军 1942 年公开的历史记录, 非字母字符在编码时跳过
#

NAVAJO_ALPHABET = {
    'A': 'WOL-LA-CHEE',     'B': 'SHUSH',           'C': 'MOASI',
    'D': 'BE',              'E': 'DZEH',            'F': 'CHUO',
    'G': 'KLIZZIE',         'H': 'LIN',             'I': 'TKIN',
    'J': 'TKELE-CHO-GI',    'K': 'KLIZZIE-YAZZIE',  'L': 'DIBEH-YAZZIE',
    'M': 'BE-TAS-TE',       'N': 'NESH-CHEE',       'O': 'NE-ASH-JE',
    'P': 'BI-SODIH',        'Q': 'CA-YEIL',         'R': 'GAH',
    'S': 'DIBEH',           'T': 'THAN-ZIE',        'U': 'SHI-DA',
    'V': 'A-KEH-DI-GLIN',   'W': 'GLOE-IH',         'X': 'AL-NA-AS-DZOH',
    'Y': 'TSAH-AS-ZIH',     'Z': 'BESH-DO-TLIZ',
}


#
# 加密: 字母替换为纳瓦霍语单词 (空格分隔)
#
def encrypt(words):
    result = []
    for ch in words.upper():
        if ch in NAVAJO_ALPHABET:
            result.append(NAVAJO_ALPHABET[ch])
    return ' '.join(result)


#
# 解密: 纳瓦霍语单词还原为字母
#
def decrypt(code):
    reverse = dict((v, k) for k, v in NAVAJO_ALPHABET.items())
    return ''.join(reverse.get(token, '?') for token in code.split())


if __name__ == '__main__':
    # 代码表见美军公开的 Navajo Code Talkers' Dictionary (1942)

    # 明文
    plaintext = 'navajo code'

    # 加密
    ciphertext = encrypt(plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext))
