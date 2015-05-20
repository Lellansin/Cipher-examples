/*
 * Caesar Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <ctype.h>

char getShiftCh(char ch, int shift, char start, char end);

/*
 * 凯撒密码
 *
 * @param char * [in]  words  要加密的字符串
 * @param int    [in]  shift  位移
 * @param char * [out] result 结果保存
 */
void caesar(char *words, int shift, char *result)
{
    int i;
    char *p = words;

    for (i = 0; *p; p++, i++)
    {
        if (isalpha(words[i]))
        {
            if (islower(words[i]))
            {
                sprintf(result, "%s%c", result, getShiftCh(words[i], shift, 'a', 'z'));
            } else
            {
                sprintf(result, "%s%c", result, getShiftCh(words[i], shift, 'A', 'Z'));
            }
        } else
        {
            sprintf(result, "%s%c", result, words[i]);
        }
    }
}

char getShiftCh(char ch, int shift, char start, char end)
{
    int diff = ((ch - start) + shift) % 26;
    if (diff >= 0) {
        return  start + diff;
    }
    else {
        return end + diff + 1;
    }
}

int main(int argc, char const *argv[])
{
    char text[] = "hello, world!";
    char cipherstext[1024], result[1024];
    int shift = -5;

    // 左移 5
    caesar(text, shift, cipherstext);
    printf("左移 %s\n", cipherstext);

    // 右移 5
    caesar(cipherstext, -shift, result);
    printf("右移 %s\n", result);

    return 0;
}
