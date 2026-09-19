/*
 * ROT-13 Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */

#include <stdio.h>
#include <ctype.h>
#include <stddef.h>

char getShiftCh(char ch, int shift, char start, char end);

/*
 * ROT-13
 *
 * @param char *   [in]  words       要加密/解密的字符串
 * @param char *   [out] result      结果保存
 * @param size_t   [in]  result_size 结果缓冲区大小
 */
void Rotation(char *words, char *result, size_t result_size)
{
    char *p    = words;
    int  shift = 13, i;

    for (i = 0; *p && (size_t)i < result_size - 1; p++, i++)
    {
        if (isalpha(words[i]))
        {
            if (islower(words[i]))
            {
                result[i] = getShiftCh(words[i], shift, 'a', 'z');
            } else
            {
                result[i] = getShiftCh(words[i], shift, 'A', 'Z');
            }
        } else
        {
            result[i] = words[i];
        }
    }
    result[i] = '\0';
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
    char ciphertext[] = "Gehzna jrag gb Jnxr Vfynaq sbe n fubeg, uvtuyl choyvpvmrq zrrgvat jvgu ZnpNeguhe. Gur PVN unq cerivbhfyl gbyq Gehzna gung Puvarfr vaibyirzrag jnf hayvxryl. ZnpNeguhe, fnlvat ur jnf fcrphyngvat, fnj yvggyr evfx. Gur trareny rkcynvarq gung gur Puvarfr unq ybfg gurve jvaqbj bs bccbeghavgl gb uryc Abegu Xbern'f vainfvba. Ur rfgvzngrq gur Puvarfr unq 300,000 fbyqvref va Znapuhevn, jvgu orgjrra 100,000-125,000 zra nybat gur Lnyh; unys pbhyq or oebhtug npebff gur Lnyh. Ohg gur Puvarfr unq ab nve sbepr; urapr, \"vs gur Puvarfr gevrq gb trg qbja gb Clbatlnat gurer jbhyq or gur terngrfg fynhtugre.\"";
    char replytext[] = "Jr PUVARFR ner abg srne.";
    char plaintext[1024], reply[1024];

    Rotation(ciphertext, plaintext, sizeof(plaintext));
    printf("解密: \n%s \n", plaintext);

    Rotation(replytext, plaintext, sizeof(plaintext));
    printf("解密: \n%s \n", plaintext);

    return 0;
}
