/*
 * Transposition Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    function transposition(matrix, words) {
        return words
            .toLowerCase()
            .replace(
                new RegExp('[\\w\\W]{1,' + matrix.length + '}', 'g'),
                function(text) {
                    var str = '';
                    for (var i = 0; i < matrix.length; i++)
                        str += text[matrix[i] - 1] || ' ';
                    return str;
                }
            );
    }

    /* -------------------- 测试 -------------------- */
    // 本例推算见《密码学基础》(西安电子科技大学出版社) 第6页

    // 明文
    var text = 'Informationsecurityisimportant';

    // 置换矩阵
    var matrix = [2, 4, 1, 3];

    // 使用矩阵置换加密字符串
    var ciphertext = transposition(matrix, text);
    console.log('密文 %s', ciphertext);

    // 置换矩阵反序即为密匙
    var secret = matrix.reverse();
    console.log('密匙 [%s]', secret);

    // 解密字符串（使用密匙置换）
    console.log('左移 %s', transposition(secret, ciphertext));

}());