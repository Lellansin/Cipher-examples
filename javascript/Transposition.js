/*
 * Transposition Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    function encrypt(matrix, words) {
        return words
            .toLowerCase()
            .replace(
                new RegExp('[\\w\\W]{1,' + matrix.length + '}', 'g'),
                function(text) {
                    var str = '';
                    for (var i = 0; i < matrix.length; i++) {
                        str += text[matrix[i] - 1] || ' ';
                    }
                    return str;
                }
            );
    }

    function decrypt(matrix, words) {
        // 置换矩阵反序即为解密密匙
        matrix = reverse(matrix);
        return encrypt(matrix, words);
    }

    var reverse = function(matrix) {
        var max = matrix.length;
        var arr = [];

        for (var i = 0; i < max; i++) {
            arr[matrix[i] - 1] = i + 1;
        }

        return arr;
    };

    /* -------------------- 测试 -------------------- */
    // 本例推算见《密码学基础》(西安电子科技大学出版社) 第6页

    // 明文
    var text = 'Informationsecurityisimportant';

    // 置换矩阵
    var key = [2, 4, 3, 1];

    // 使用矩阵置换加密字符串
    var ciphertext = encrypt(key, text);
    console.log('密文 %s', ciphertext);

    // 解密字符串（使用密匙置换）
    console.log('左移 %s', decrypt(key, ciphertext));

}());
