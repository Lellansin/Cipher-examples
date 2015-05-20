/*
 * Vigenere Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define A 65
#define TABLE_WIDTH 26

char table[TABLE_WIDTH][TABLE_WIDTH];

int initTable();
int printTable();

/*
 * 加密
 *
 * @param key    密钥
 * @param src    待加密的字符串
 * @param dest   经过加密后的字符串
 */
int encrypt(char* key, char* src, char* dest)
{
	char *pSrc = src;
	char *pKey = key;
	char *pDest = dest;

	do {
		if (!isalpha(*pSrc))
		{
			continue;
		}
		*pDest++ = table[toupper(*pKey) - A][toupper(*pSrc) - A];

		if (!(*(++pKey)))
			pKey = key;
	} while (*pSrc++);

	dest[strlen(src)] = 0;
	return 1;
}

/*
 * 解密
 *
 * @param key    密钥
 * @param src    待解密的字符串
 * @param dest   经过解密后的字符串
 */
int decrypt(char* key, char* src, char* dest)
{	char *pSrc = src;
	char *pKey = key;
	char *pDest = dest;
	char offset;

	do {
		offset = (*pSrc) - toupper(*pKey);
		offset = offset >= 0 ? offset : offset + TABLE_WIDTH;
		*pDest++ = tolower(A + offset);

		if (!(*(++pKey)))
			pKey = key;
	} while (*pSrc++);

	dest[strlen(src)] = 0;
	return 1;
}

int main()
{
	// 本例推算见《密码学基础》(西安电子科技大学出版社) 第5页
	char secret[256] = "computer";
	char text[256] = "block cipher design principles";
	char ciphertext[256];
	char output[256];

	// 初始化密表
	initTable();
	printTable();

	// 根据密匙加密
	encrypt(secret, text, ciphertext);
	printf("密文 [%s]\n", ciphertext);

	// 根据密匙解密
	decrypt(secret, ciphertext, output);
	printf("解密 [%s]\n", output);

	return 0;
}

/*
 * 初始化维吉尼亚方阵
 */
int initTable()
{
	int i, j;
	for (i = 0; i < TABLE_WIDTH; i++)   {
		for (j = 0; j < TABLE_WIDTH; j++)    {
			table[i][j] = A + (i + j) % TABLE_WIDTH;
		}
	}
	return 1;
}

int printTable()
{
	int i, j;
	for (i = 0; i < TABLE_WIDTH; i++)   {
		for (j = 0; j < TABLE_WIDTH; j++)    {
			printf("%c ", table[i][j]);
		}
		printf("\n");
	}
	return 1;
}