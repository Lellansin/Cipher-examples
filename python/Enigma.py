# -*- coding: utf-8 -*-
#
# Enigma Cipher (Enigma I / M3 三转子)
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

# 转子接线 (A 对应第一位) 与换位字母 (自身步进经过该字母时推动左邻转子)
ROTORS = {
    'I':   ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'),
    'II':  ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'),
    'III': ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'),
    'IV':  ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'K'),
    'V':   ('VZBRGITYUPSDNHLXAWMJQOFECK', 'A'),
}

# 反射器
REFLECTORS = {
    'A': 'EJMZALYXVBWFCRQUONTSPIKHGD',
    'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
}


def _inverse(wiring):
    result = [0] * 26
    for i, c in enumerate(wiring):
        result[c] = i
    return result


#
# 初始化机器状态
#
# rotors    从左到右的转子名, 如 ('I', 'II', 'III')
# positions 起始位置, 如 'AAA'
# rings     环设置 (内接线相对字母环的偏移)
# plugboard 插接板, 如 'AM FI NV' 表示 A<->M, F<->I, N<->V
#
def create(rotors=('I', 'II', 'III'), reflector='B', positions='AAA', rings='AAA', plugboard=''):
    state = {
        'wiring': [], 'inverse': [], 'turnover': [], 'position': [],
        'reflector': REFLECTORS[reflector], 'plug': {},
    }
    for i, name in enumerate(rotors):
        wiring, turnover = ROTORS[name]
        state['wiring'].append([ord(c) - 65 for c in wiring])
        state['inverse'].append(_inverse(state['wiring'][i]))
        state['turnover'].append(ord(turnover) - 65)
        state['position'].append(ord(positions[i]) - ord('A') - (ord(rings[i]) - ord('A')))

    pairs = plugboard.upper().replace(' ', '')
    for i in range(0, len(pairs) - 1, 2):
        a, b = ord(pairs[i]) - 65, ord(pairs[i+1]) - 65
        state['plug'][a] = b
        state['plug'][b] = a
    return state


#
# 步进: 按键时右转子前进一格; 双跳步 - 中转子走到自身换位字母时
# 与左转子同时进位, 右转子走到换位字母时推动中转子
#
def step(state):
    p, t = state['position'], state['turnover']
    n = len(p)
    if p[n-2] == t[n-2]:
        p[n-2] = (p[n-2] + 1) % 26
        p[n-3] = (p[n-3] + 1) % 26
    elif p[n-1] == t[n-1]:
        p[n-2] = (p[n-2] + 1) % 26
    p[n-1] = (p[n-1] + 1) % 26


#
# 加密单个字母 (步进 -> 插接板 -> 转子正向 -> 反射器 -> 转子反向 -> 插接板)
#
def encrypt_letter(state, ch):
    step(state)
    code = ord(ch) - 65
    code = state['plug'].get(code, code)

    for i in reversed(range(len(state['wiring']))):
        pos = state['position'][i]
        code = (state['wiring'][i][(code + pos) % 26] - pos) % 26

    code = ord(state['reflector'][code]) - 65

    for i in range(len(state['wiring'])):
        pos = state['position'][i]
        code = (state['inverse'][i][(code + pos) % 26] - pos) % 26

    code = state['plug'].get(code, code)
    return chr(code + 65)


#
# 加密 (恩尼格玛是自反密码, 加密与解密是同一操作)
#
def encrypt(state, words):
    ciphertext = ''
    for ch in words.upper():
        if 'A' <= ch <= 'Z':
            ciphertext += encrypt_letter(state, ch)
    return ciphertext


# 恩尼格玛加解密是同一个操作
decrypt = encrypt


if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Enigma_rotor_details
    # 转子 I/II/III (左起), 反射器 B, 环设置与起始位置均为 AAA 时
    # wiki 原文: typing AAAAA will produce the encoded sequence BDZGO

    enigma = create(rotors=('I', 'II', 'III'), reflector='B')

    # 加密
    ciphertext = encrypt(enigma, 'AAAAA')
    print(ciphertext)

    # 解密 (重置到相同初始状态即为解密)
    enigma = create(rotors=('I', 'II', 'III'), reflector='B')
    print(decrypt(enigma, ciphertext))

    # 带插接板与环设置的完整示例
    enigma = create(rotors=('I', 'III', 'II'), reflector='B',
                    positions='QEV', rings='BDZ', plugboard='AM FI NV')
    message = 'attack at dawn'
    ciphertext = encrypt(enigma, message)
    print(ciphertext)
    enigma = create(rotors=('I', 'III', 'II'), reflector='B',
                    positions='QEV', rings='BDZ', plugboard='AM FI NV')
    print(decrypt(enigma, ciphertext))
