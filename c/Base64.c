#include <stdio.h>
#include <string.h>

// 密表
const char table[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                            "abcdefghijklmnopqrstuvwxyz"
                            "0123456789+/";

inline size_t encoded_size(size_t size) {
  return ((size + 2 - ((size + 2) % 3)) / 3 * 4);
}

/*
 * Base64 编码
 *
 * @param char * [in]  src   要编码的字符串
 * @param char * [out] dst   编码后的内容保存的字符串
 */
void encode(const char* src, char* dst) {
  size_t slen = strlen(src);

  unsigned a;
  unsigned b;
  unsigned c;
  unsigned i;
  unsigned k;
  unsigned n;

  i = 0;
  k = 0;
  n = slen / 3 * 3;

  while (i < n) {
    a = src[i + 0] & 0xff;
    b = src[i + 1] & 0xff;
    c = src[i + 2] & 0xff;

    dst[k + 0] = table[a >> 2];
    dst[k + 1] = table[((a & 3) << 4) | (b >> 4)];
    dst[k + 2] = table[((b & 0x0f) << 2) | (c >> 6)];
    dst[k + 3] = table[c & 0x3f];

    i += 3;
    k += 4;
  }

  if (n != slen) {
    switch (slen - n) {
      case 1:
        a = src[i + 0] & 0xff;
        dst[k + 0] = table[a >> 2];
        dst[k + 1] = table[(a & 3) << 4];
        dst[k + 2] = '=';
        dst[k + 3] = '=';
        break;
      case 2:
        a = src[i + 0] & 0xff;
        b = src[i + 1] & 0xff;
        dst[k + 0] = table[a >> 2];
        dst[k + 1] = table[((a & 3) << 4) | (b >> 4)];
        dst[k + 2] = table[(b & 0x0f) << 2];
        dst[k + 3] = '=';
        break;
    }
  }
}

/*
 * Base64 解码
 *
 * @param char * [in]  src   要编码的字符串
 * @param char * [out] dst   编码后的内容保存的字符串
 */
void decode(char *ciphertext, char *output) {

}

int main(int argc, char const *argv[])
{
  char text[256] = "Hello, world!";
  char ciphertext[256];
  char output[256];

  // 按照 base64 格式编码
  encode(text, ciphertext);
  printf("编码 [%s]\n", ciphertext);

  // TODO 解码
  decode(ciphertext, output);

  return 0;
}
