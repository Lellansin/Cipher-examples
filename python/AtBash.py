# -*- coding: utf-8 -*-
#
# AtBash Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 埃特巴什密码: 按字母表倒序映射, A<->Z, B<->Y, C<->X ...
#
def atbash(words):
    result = ''
    for ch in words:
        if 'a' <= ch <= 'z':
            result += chr(ord('a') + ord('z') - ord(ch))
        elif 'A' <= ch <= 'Z':
            result += chr(ord('A') + ord('Z') - ord(ch))
        else:
            result += ch
    return result

# 埃特巴什密码加解密是同一个操作
decrypt = atbash

if __name__ == '__main__':
    # 本例推算见 http://en.wikipedia.org/wiki/Atbash

    # 明文
    plaintext = 'hello world, this is Atbash cipher.'

    # 加密
    ciphertext = atbash(plaintext)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext))
