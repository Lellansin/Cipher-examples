/*
 * Polybius Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <stdlib.h> // for rand
#include <time.h> // for time
#include <string.h> // for memcpy, strlen
#include <ctype.h> // for toupper, tolower

#define TABLE_WIDTH 5
#define ALPHABET {"ABCDEFGHIKLMNOPQRSTUVWXYZ"}

enum TEXT_TYPE { WITH_BLANK, NO_BLANK };

static int  randomInt(int min, int max);          // 随机一个整数 x (min <= x < max)
static void printTable(char *table);              // 打印棋盘
static int  getTableIndex(char a, char *table);   // 获取棋盘对应字母的数字
static char getTableChar(int index, char *table); // 获取棋盘对应数字的字母

/*
 * 生成棋盘
 */
char * generateTable()
{
    int i, j, r;
    char tmp[] = ALPHABET;
    char *table = malloc(TABLE_WIDTH * TABLE_WIDTH);

    // 随机初始化
    for (i = 0; i < TABLE_WIDTH; i++)
    {
        for (j = 0; j < TABLE_WIDTH; j++)
        {
            while (1)
            {
                r = randomInt(0, 25);
                if (tmp[r] != 0)
                {
                    table[i * TABLE_WIDTH + j] = tmp[r];
                    tmp[r] = 0;
                    break;
                }
            }
        }
    }

    return table;
}

/*
 * 加密
 */
char * encrypt(char *table, char *words, enum TEXT_TYPE type)
{
    char *ciphertext, *format;
    int *arr, i, index;
    int count = 0, len = strlen(words);

    // 保存结果数组的地方
    arr = (int *)malloc(len * sizeof(int));
    memset(arr, 0, len * sizeof(int)); // 初始化内存

    for (i = 0; i < len; i++)
    {
        // 字符转大写后获取对应棋盘坐标
        index = getTableIndex(toupper(words[i]), table);

        // 保存坐标
        if (index)
        {
            arr[count++] = index;
        }
    }

    // 保存密文的地方
    ciphertext = (char *)malloc(count * 3 + 1);
    memset(ciphertext, 0, count * 3 + 1); // 初始化内存

    if (type == WITH_BLANK)
    {
        format = "%s%-3d";
    } else {
        format = "%s%d";
    }

    for ( i = 0; count--; i++)
    {
        sprintf(ciphertext, format, ciphertext, arr[i]);
    }

    return ciphertext;
}

/*
 * 解密
 */
char * decrypt(char *table, char *numbers)
{
    char *result, *tmpstr, tmpch, *p;
    int len = strlen(numbers), count = 0;
    int i, num;

    // 备份字符串
    tmpstr = (char *)malloc(len + 1);
    strcpy(tmpstr, numbers);

    // 保存解密后字符串的地方
    result = (char *)malloc(len / 3 + 1);
    memset(result, 0, len / 3 + 1); // 初始化内存

    for (i = 0; i < (len - 1); i++) {
        num = 0;
        p = tmpstr + i;

        if (isdigit(tmpstr[i]) && isdigit(tmpstr[i + 1])) {
            tmpch = tmpstr[i + 2];
            tmpstr[i + 2] = '\0';
            sscanf(p, "%2d", &num);
            tmpstr[i + 2] = tmpch;
            i++;
        }

        if (num > 10)
        {
            result[count++] = getTableChar(num, table);
        }
    }

    return result;
}

int main(int argc, char const *argv[])
{
    char *table;
    char *text1 = "hello world",
          *text2 = "Glad to meet you, polybius cipher.";
    char *ciphertext1, *parsetext1,
         *ciphertext2, *parsetext2;

    printf("随机生成棋盘:\n");
    table = generateTable();
    printTable(table);

    printf("棋盘加密1\n");
    ciphertext1 = encrypt(table, text1, WITH_BLANK);
    printf("原文 %s\n", text1);
    printf("密文 %s\n", ciphertext1);

    printf("根据棋盘解密\n");
    parsetext1 = decrypt(table, ciphertext1);
    printf("结果 %s\n", parsetext1);

    printf("\n棋盘加密2\n");
    ciphertext2 = encrypt(table, text2, NO_BLANK);
    printf("原文 %s\n", text2);
    printf("密文 %s\n", ciphertext2);

    printf("根据棋盘解密\n");
    parsetext2 = decrypt(table, ciphertext2);
    printf("结果 %s\n", parsetext2);

    free(table);
    free(ciphertext1);
    free(parsetext1);
    free(ciphertext2);
    free(parsetext2);
    return 0;
}


/*
 * 随机一个整数 x (min <= x < max)
 */
static int randomInt(int min, int max) // 随机一个整数 x (min <= x < max)
{
    static int r = 0;
    srand(time(NULL) + r);
    r = rand();
    return (r % max + min);
}

/*
 * 获取棋盘对应字母的数字
 */
static int getTableIndex(char a, char *table)
{
    int i, j;

    for (i = 0; i < TABLE_WIDTH; i++)
    {
        for (j = 0; j < TABLE_WIDTH; j++)
        {
            if (a == table[i * TABLE_WIDTH + j])
            {
                return (i + 1) * 10 + (j + 1);
            }
        }
    }
    return 0;
}

/*
 * 获取棋盘对应数字的字母
 */
static char getTableChar(int index, char *table)
{
    int i = index / 10 - 1,
        j = index % 10 - 1;
    return tolower(table[i * TABLE_WIDTH + j]);
}

/*
 * 打印棋盘
 */
static void printTable(char *table)
{
    int i, j;

    for (i = 0; i <= TABLE_WIDTH; i++)
        if (i)
            printf("%d ", i);
        else
            printf("  ");

    printf("\n");

    for (i = 0; i < TABLE_WIDTH; i++)
    {
        printf("%d ", i + 1);
        for (j = 0; j < TABLE_WIDTH; j++)
        {
            printf("%c ", table[i * TABLE_WIDTH + j]);
        }
        printf("\n");
    }

    printf("\n");
}

