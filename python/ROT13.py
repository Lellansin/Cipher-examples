# -*- coding: utf-8 -*-
#
# ROT-13 Cipher
# 
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#
from Caesar import caesar

# 
# Rotaion
# 
def rotaion(words):
    return caesar(words, 13)


if __name__ == '__main__':
    # ROT-n 就是凯撒密码位移 n

    # 密文
    text = "Jul qvq gur puvpxra pebff gur ebnq?\nGb trg gb gur bgure fvqr!"
    
    # 解密
    plaintext = rotaion(text)

    # 明文
    print('解密: ' + plaintext)

    # 加密对比
    print('对比: ' + str(rotaion(plaintext) == text))
