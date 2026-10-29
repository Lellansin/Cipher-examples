# -*- coding: utf-8 -*-
#
# Homophonic Substitution Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 同音替换密码: 高频字母对应多个替换符号, 低频字母对应少量符号
# 使密文中各符号出现频率趋近均匀, 对抗频率分析
# 本例使用按英语字母频率 (E~12%, T~9%, ...) 分配的确定性数字符号表
# 教学实现: 同一字母第 i 次出现时轮换使用其符号列表中的第 i 个
# (真实实现通常随机挑选)
#

# 按英语字母频率分配的同音符号数量表
FREQUENCY = {
    'E': 12, 'T': 9, 'A': 8, 'O': 8, 'I': 8, 'N': 7, 'S': 6, 'H': 6,
    'R': 6, 'D': 4, 'L': 4, 'C': 3, 'U': 3, 'M': 3, 'W': 2, 'F': 2,
    'G': 2, 'Y': 2, 'P': 2, 'B': 1, 'V': 1, 'K': 1, 'J': 1, 'X': 1,
    'Q': 1, 'Z': 1,
}


#
# 生成字母 -> 符号列表的映射 (符号为互不重复的连续数字)
#
def generate_table():
    table, symbol = {}, 0
    for letter, count in FREQUENCY.items():
        table[letter] = list(range(symbol, symbol + count))
        symbol += count
    return table


#
# 加密: 字母 -> 数字 (空格分隔), 非字母原样保留
#
def encrypt(words):
    table = generate_table()
    counters = dict.fromkeys(table, 0)
    result = ''
    for ch in words.upper():
        if ch in table:
            symbols = table[ch]
            result += str(symbols[counters[ch] % len(symbols)]) + ' '
            counters[ch] += 1
        elif ch == ' ':
            result += '/ '
        else:
            result += ch + ' '
    return result.strip()


#
# 解密
#
def decrypt(numbers):
    table = generate_table()
    reverse = {}
    for letter, symbols in table.items():
        for s in symbols:
            reverse[s] = letter
    result = ''
    for token in numbers.split():
        if token.isdigit():
            result += reverse.get(int(token), '?')
        elif token == '/':
            result += ' '
        else:
            result += token
    return result


if __name__ == '__main__':
    # 同音替换原理见 https://en.wikipedia.org/wiki/Homophonic_cipher

    # 明文
    plaintext = 'the letter e appears twelve times per hundred'

    # 加密 (共 104 个数字符号, 高频字母对应更多符号)
    ciphertext = encrypt(plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext))
