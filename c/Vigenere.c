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
#define TABLEWIDTH 26

char table[TABLEWIDTH][TABLEWIDTH];

int initTable();
int printTable();
int encode(char* key, char* src, char* dest);
int dncode(char* key, char* src, char* dest);

/*
 * 加密
 *
 * @param key    密钥
 * @param src    待加密的字符串
 * @param dest   经过加密后的字符串
 */
int encode(char* key, char* src, char* dest)
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
int dncode(char* key, char* src, char* dest)
{	char *pSrc = src;
	char *pKey = key;
	char *pDest = dest;
	char offset;

	do {
		offset = (*pSrc) - toupper(*pKey);
		offset = offset >= 0 ? offset : offset + TABLEWIDTH;
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
	encode(secret, text, ciphertext);
	printf("密文 [%s]\n", ciphertext);

	// 根据密匙解密
	dncode(secret, ciphertext, output);
	printf("解密 [%s]\n", output);

	return 0;
}

/*
 * 初始化维吉尼亚方阵
 */
int initTable()
{
	int i, j;
	for (i = 0; i < TABLEWIDTH; i++)   {
		for (j = 0; j < TABLEWIDTH; j++)    {
			table[i][j] = A + (i + j) % TABLEWIDTH;
		}
	}
	return 1;
}

int printTable()
{
	int i, j;
	for (i = 0; i < TABLEWIDTH; i++)   {
		for (j = 0; j < TABLEWIDTH; j++)    {
			printf("%c ", table[i][j]);
		}
		printf("\n");
	}
	return 1;
}