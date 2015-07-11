/*
 * Autokey Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define A 65
#define TABLE_WIDTH 26

int initTable();
void copy(char *dest, char *src, int len);

/*
 * 加密
 *
 * @param key    密钥
 * @param src    待加密的字符串
 * @param dest   经过加密后的字符串
 */
int encrypt(char* key, char* src, char* dest)
{
	char table[TABLE_WIDTH][TABLE_WIDTH];
	char *pSrc = src;
	char *pKey = key;
	char *pDest = dest;

	initTable(table);

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
		*pDest++ = A + offset;

		if (!(*(++pKey)))
			pKey = key;
	} while (*pSrc++);

	dest[strlen(src)] = 0;
	return 1;
}

void getKey(char *key, char *text, char *keyword)
{
	int total = strlen(text);
	int len = strlen(keyword);

	if (len)
	{
		copy(key, keyword, len);
	}

	copy(key + len, text, total - len);
}

void copy(char *dest, char *src, int len)
{
	while (len-- > 0)
	{
		if (isalpha(*src))
		{
			*dest++ = toupper(*src);
		}

		src++;
	}
}

int main()
{
	// 本例推算见 http://www.cryptool-online.org/index.php?option=com_content&view=article&id=104&Itemid=127&lang=en
	char text[256] = "THIS IS A SECRET TEXT";
	char key[256] = "";
	char keyword[256] = "KEY";

	char ciphertext[256];
	char output[256];

	// 获取自动密匙
	getKey(key, text, keyword);
	printf("密匙 [%s]\n", key);

	// 根据密匙加密
	encrypt(key, text, ciphertext);
	printf("密文 [%s]\n", ciphertext);

	// 根据密匙解密
	decrypt(key, ciphertext, output);
	printf("解密 [%s]\n", output);

	return 0;
}

/*
 * 初始化维吉尼亚方阵
 */
int initTable(char table[TABLE_WIDTH][TABLE_WIDTH])
{
	int i, j;
	for (i = 0; i < TABLE_WIDTH; i++)   {
		for (j = 0; j < TABLE_WIDTH; j++)    {
			table[i][j] = A + (i + j) % TABLE_WIDTH;
		}
	}
	return 1;
}
