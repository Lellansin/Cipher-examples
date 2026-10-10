# -*- coding: utf-8 -*-
#
# Pollux Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# 摩斯电码表 (与 javascript/Morse.js 一致)
MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}

#
# 波卢克斯密码: 先把明文转成摩斯电码 (字母间 x, 单词间 xx),
# 再按密钥把每个摩斯符号 (点/划/x) 替换为数字
# 密钥为长度 10 的字符串, 第 i 位表示数字 i 对应的摩斯符号, 如 '..--xx....'
# (ACA: American Cryptogram Association)
#

#
# 明文转摩斯电码
#
def to_morse(words):
    result = []
    for word in words.upper().split():
        codes = [MORSE[ch] for ch in word if ch in MORSE]
        if codes:
            result.append('x'.join(codes))
    return 'xx'.join(result)


#
# 加密
#
def encrypt(key, words):
    if len(key) != 10:
        raise ValueError('密钥必须是长度为 10 的字符串')
    morse = to_morse(words)
    return ''.join(str(key.index(sym)) for sym in morse)


#
# 解密
#
def decrypt(key, numbers):
    if len(key) != 10:
        raise ValueError('密钥必须是长度为 10 的字符串')
    morse = ''.join(key[int(d)] for d in str(numbers))
    text = ''
    for word in morse.split('xx'):
        for code in word.split('x'):
            for letter, val in MORSE.items():
                if val == code:
                    text += letter
                    break
        text += ' '
    return text.strip()


if __name__ == '__main__':
    # Pollux 规则见 American Cryptogram Association / dCode.fr

    # 明文
    plaintext = 'sos'

    # 密钥 (数字 0-9 对应的摩斯符号)
    key = '..--xx....'

    # 加密
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(key, ciphertext))
