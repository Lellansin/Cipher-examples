/*
 * Double Transposition Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    /*
     * 加密
     */
    function encrypt(matrix, words) {
        var count = 0;
        var len = matrix.length;
        var ciphertext = '';

        for (var i = 0; i < len; i++) {
            var pos = getPos(matrix, i + 1);

            do {
                var ch = words[pos + len * count++];
                if (ch) {
                    ciphertext += ch;
                } else {
                    break;
                }
            } while (true);

            count = 0;
        }

        return ciphertext;
    }

    /*
     * 解密
     */
    function decrypt(matrix, words) {
        var plaintext = '',
            matrix_len = matrix.length,
            size = Math.floor(words.length / matrix_len),
            remainder = words.length % matrix_len;

        // 获取长度表
        var arr = [];
        for (var i = 0; i < matrix_len; i++) {
            arr[matrix[i] - 1] = size + (remainder-- > 0 ? 1 : 0);
        }

        // 根据长度获取纵向数组
        var vertical = [];
        for (var cur = 0, j = 0; j < arr.length; j++) {
            var str = words.substr(cur, arr[j]);
            vertical.push(str.split(''));
            cur += arr[j];
        }

        // 将纵向数组顺序还原
        var revr = reverse(matrix);
        for (var row = 0; row < (size + 1); row++) {
            for (var col = 0; col < matrix_len; col++) {
                var pos = getPos(revr, col + 1);
                var list = vertical[pos];
                plaintext += list.shift() || '';
            }
        }

        return plaintext;
    }

    var getPos = function(matrix, num) {
        for (var i = matrix.length - 1; i >= 0; i--) {
            if (matrix[i] == num) {
                return i;
            }
        }
        return null;
    };

    var reverse = function(matrix) {
        var max = matrix.length;
        var arr = [];

        for (var i = 0; i < max; i++) {
            arr[matrix[i] - 1] = i + 1;
        }

        return arr;
    };

    /* -------------------- 测试 -------------------- */
    // http://en.wikipedia.org/wiki/Transposition_cipher#Double_transposition

    // 明文
    var text = 'EVLNACDTESEAROFODEECWIREE';

    // 置换矩阵
    var key = [5, 6, 4, 2, 3, 1];

    // 使用矩阵置换加密字符串
    var ciphertext = encrypt(key, text);
    console.log('密文 %s', ciphertext);

    // 解密字符串（使用密匙置换）
    console.log('解密 %s', decrypt(key, ciphertext));

}());