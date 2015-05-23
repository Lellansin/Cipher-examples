/*
 * Four-Square Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var FourSquare = {};

    // 默认密表
    var table = 'ABCDEFGHIJKLMNOPRSTUVWXYZ';

    /*
     * 生成棋盘
     */
    FourSquare.generateTable = function(key) {
        var alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ';
        var table = '';
        key = key || '';
        key = key.replace(/[\W]/, '').toUpperCase();

        for (var row = 0; row < 5; row++) {
            for (var col = 0; col < 5; col++) {
                if (key.length) {
                    table += key[0]
                    alphabet = alphabet.replace(key[0], '')
                    key = key.replace(new RegExp(key[0], 'g'), '')
                } else {
                    table += alphabet[0];
                    alphabet = alphabet.substring(1);
                }
            }
        }
        return table;
    };

    /*
     * 打印棋盘
     */
    FourSquare.printTable = function(table) {
        var str = '  1 2 3 4 5 \n';
        for (var y = 0; y < 5; y++) {
            str += (y + 1) + ' ';
            for (var x = 0; x < 5; x++) {
                str = str + table[y * 5 + x] + ' ';
            }
            str += '\n';
        }
        console.log(str);
    };

    /*
     * 加密
     */
    FourSquare.encrypt = function(keys, text) {
        var R = FourSquare.generateTable(key[0]);
        var L = FourSquare.generateTable(key[1]);

        return text
            .toUpperCase()
            .replace(/[\WQ]/g, '')
            .replace(/[\w]{1,2}/g, function(digraphs) {
                var a = position(table, digraphs[0]);
                var b = position(table, digraphs[1] || 'X');
                return R[a[0] * 5 + b[1]] + L[b[0] * 5 + a[1]];
            });
    };

    /*
     * 解密
     */
    FourSquare.decrypt = function(keys, text) {
        var R = FourSquare.generateTable(key[0]);
        var L = FourSquare.generateTable(key[1]);

        return text
            .toUpperCase()
            .replace(/[\WQ]/g, '')
            .replace(/[\w]{1,2}/g, function(digraphs) {
                var a = position(R, digraphs[0]);
                var b = position(L, digraphs[1] || 'X');
                return table[a[0] * 5 + b[1]] + table[b[0] * 5 + a[1]];
            });
    };

    var position = function(table, ch) {
        var index = table.indexOf(ch);
        return [Math.floor(index / 5), index % 5];
    }

    /* -------------------- 测试 --------------------- */
    // 本例推算见 http://en.wikipedia.org/wiki/Four-square_cipher

    // 明文
    var text = 'help me obiwankenobi';

    // 密匙
    var key = ['example', 'keyword'];

    // 加密
    var ciphertext = FourSquare.encrypt(table, text);
    console.log(ciphertext);

    // 解密
    console.log(FourSquare.decrypt(table, ciphertext));

}());
