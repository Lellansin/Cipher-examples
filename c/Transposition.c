/*
 * Transposition Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <ctype.h> // tolower
#include <stdlib.h> // for malloc
#include <string.h> // for strlen

/*
 * 加密
 *
 * @param char * [in]  key    密匙
 * @param char * [in]  words  要加密的字符串
 * @param char * [out] result 结果保存
 */
void encrypt(char *key, char *words, char *cipher)
{
    int kLen = strlen(key);
    int wLen = strlen(words);
    int i, j, pos;

    for (i = 0; i < wLen; i += kLen )
    {
        for (j = 0; j < kLen; ++j)
        {
            pos = key[j] - '0' - 1 + i;

            if (pos < wLen)
            {
                sprintf(cipher, "%s%c", cipher, tolower(words[pos]));
            }
            else
            {
                sprintf(cipher, "%s ", cipher);
            }
        }
    }
}

/*
 * 解密
 *
 * @param char * [in]  key    密匙
 * @param char * [in]  words  要解密的字符串
 * @param char * [out] result 结果保存
 */
void decrypt(char *key, char *cipher, char *plaintext)
{
    int  len  = strlen(key), i;
    char *arr = (char*)malloc(sizeof(char) * len);

    for (i = 0; i < len; ++i)
        arr[(key[i] - '0') - 1] = '0' + i + 1;

    encrypt(arr, cipher, plaintext);
    free(arr);
}

int main(int argc, char const *argv[])
{
    // 本例推算见《密码学基础》(西安电子科技大学出版社) 第6页

    char text[] = "Informationsecurityisimportant";
    char  key[] = "2413";
    char ciphertext[1024], plaintext[1024];

    encrypt(key, text, ciphertext);
    printf("解密: %s \n", ciphertext);

    decrypt(key, ciphertext, plaintext);
    printf("解密: %s \n", plaintext);

    return 0;
}
