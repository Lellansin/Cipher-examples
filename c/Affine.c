/*
 * Affine Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define WIDTH 26

int  gcd(int a, int b);
char shift(int *key, char ch);
char unshift(int *key, char ch);
int  modInverse(int a, int m);

/*
 * 加密
 *
 * @param key    密钥 { a, b }
 * @param src    待加密的字符串
 * @param dest   经过加密后的字符串
 */
char * encrypt(int* key, char* src, char* dest)
{
    char *pSrc  = src;
    char *pDest = dest;

    if (gcd(key[0], WIDTH) != 1)
    {
        printf("Error: a 与 m 不互素");
        exit(-1);
    }

    for (int i = 0; *pSrc; ++i, ++pSrc, ++pDest)
    {
        if (!isalpha(*pSrc))
            continue;

        *pDest = shift(key, toupper(*pSrc));
    }

    return dest;
}

/*
 * 解密
 *
 * @param key    密钥 { a, b }
 * @param src    待解密的字符串
 * @param dest   经过解密后的字符串
 */
char * decrypt(int* key, char* src, char* dest)
{
    char *pSrc  = src;
    char *pDest = dest;
    int  arr[2] = { modInverse(key[0], WIDTH), -key[1] };

    for (int i = 0; *pSrc; ++i, ++pSrc, ++pDest)
    {
        if (!isalpha(*pSrc))
            continue;

        *pDest = unshift(arr, toupper(*pSrc));
    }

    return dest;
}

int main(int argc, char const *argv[])
{
    // 本例推算见 http://en.wikipedia.org/wiki/Affine_cipher

    int  key[]  = { 5, 8 };       // 密匙
    char text[] = "AFFINECIPHER"; // 明文
    char ciphertext[1024], result[1024];

    // 加密
    encrypt(key, text, ciphertext);
    printf("%s\n", ciphertext);

    // 解密
    decrypt(key, ciphertext, result);
    printf("%s\n", result);

    return 0;
}

/*
 * E(x) = (ax + b) mod m
 */
char shift(int *key, char ch)
{
    int offset = ch - 'A';
    return (key[0] * offset + key[1]) % WIDTH + 'A';
}

/*
 * D(x) = a^{-1}(x - b) mod m
 */
char unshift(int *key, char ch)
{
    int offset = ch - 'A';
    return (((key[0] * (offset + key[1])) % WIDTH + WIDTH) % WIDTH) + 'A';
}

/*
 * 判断 a 与 b 是否互素
 */
int gcd(int a, int b)
{
    int tmp;
    while (a != 0)
    {
        tmp = a;
        a = b % a;
        b = tmp;
    }
    return b;
}

/*
 * 求 a 在密表中的乘法逆
 */
int modInverse( int a, int m)
{
    int x1, x2, x3, y1, y2, y3, t1, t2, t3, q;
    x1 = y2 = 1, x2 = y1 = 0;
    x3 = ( a >= m ) ? a : m;
    y3 = ( a >= m ) ? m : a;

    while ( 1 )
    {
        if ( y3 == 0 )
        {
            return x3;
        }
        else if ( y3 == 1 )
        {
            return y2;
        }
        q = x3 / y3;
        t1 = x1 - q * y1, t2 = x2 - q * y2, t3 = x3 - q * y3;
        x1 = y1, x2 = y2, x3 = y3;
        y1 = t1, y2 = t2, y3 = t3;
    }
}
