# -*- coding: utf-8 -*-
#
# Skip Cipher
#
# @author  lellansin <lellansin@gmail.com>
# @website http://www.lellansin.com/tutorials/ciphers
#

#
# 跳步密码: 从 start 位置起, 每隔 step 取一个字母 (到尾部后回绕继续),
# 直到取完全部字母; 是一种环状置换密码
#

#
# 加密
#
def encrypt(words, step, start=0):
    length = len(words)
    if length < 2 or step % length == 0:
        return words

    visited = [False] * length
    order = []
    idx = start % length
    while len(order) < length:
        if not visited[idx]:
            visited[idx] = True
            order.append(idx)
            idx = (idx + step) % length
        else:
            # 当前环已走完 (step 与长度有公因数), 跳到下一个未访问位置继续
            while visited[idx]:
                idx = (idx + 1) % length
    return ''.join(words[i] for i in order)


#
# 解密: 求出同一取字顺序, 把密文字母放回原位
#
def decrypt(words, step, start=0):
    length = len(words)
    if length < 2 or step % length == 0:
        return words

    visited = [False] * length
    order = []
    idx = start % length
    while len(order) < length:
        if not visited[idx]:
            visited[idx] = True
            order.append(idx)
            idx = (idx + step) % length
        else:
            # 当前环已走完 (step 与长度有公因数), 跳到下一个未访问位置继续
            while visited[idx]:
                idx = (idx + 1) % length

    result = [''] * length
    for k, i in enumerate(order):
        result[i] = words[k]
    return ''.join(result)


if __name__ == '__main__':
    # 手工推算示例: HELLOWORLD, step=3
    # 取字顺序 0,3,6,9,2,5,8,1,4,7 -> H L O D L W L E O R

    # 明文
    plaintext = 'helloworld'

    # 步长
    step = 3

    # 加密
    ciphertext = encrypt(plaintext, step)
    print(ciphertext)

    # 解密
    print(decrypt(ciphertext, step))
