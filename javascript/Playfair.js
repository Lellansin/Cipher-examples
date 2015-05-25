/*
 * Playfair Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Playfair = {};

    /*
     * 生成密表
     */
    Playfair.generateTable = function(key) {
        var alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
        var table = '';

        key = key ? key.toUpperCase().replace(/[\WJ]/, '') : '';

        for (var i = 0; i < 25; i++) {
            if (key.length) {
                table += key[0];
                alphabet = alphabet.replace(key[0], '');
                key = key.replace(new RegExp(key[0], 'g'), '');
            } else {
                table += alphabet[0];
                alphabet = alphabet.substring(1);
            }
        }
        return table;
    };

    /*
     * 打印密表
     */
    Playfair.printTable = function(table) {
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
    Playfair.encrypt = function(key, text) {
        var table = Playfair.generateTable(key);

        return text
            .toUpperCase()
            .replace(/[\WJ]/g, '')
            .each(function(cur, next) {
                if (cur == next) return cur + 'X';
            })
            .replace(/[\w]{1,2}/g, function(digraphs) {
                var a = position(table, digraphs[0]);
                var b = position(table, digraphs[1] || 'X');

                if (a[0] == b[0]) {
                    return table[a[0] * 5 + (a[1] + 1) % 5] + table[b[0] * 5 + (b[1] + 1) % 5];
                } else if (a[1] == b[1]) {
                    return table[(a[0] + 1) % 5 * 5 + a[1]] + table[(b[0] + 1) % 5 * 5 + b[1]];
                } else {
                    return table[a[0] * 5 + b[1]] + table[b[0] * 5 + a[1]];
                }
            });
    };

    /*
     * 解密
     */
    Playfair.decrypt = function(key, text) {
        var table = Playfair.generateTable(key);

        return text
            .toUpperCase()
            .replace(/[\WJ]/g, '')
            .replace(/[\w]{1,2}/g, function(digraphs) {
                var a = position(table, digraphs[0]);
                var b = position(table, digraphs[1]);

                if (a[0] == b[0]) {
                    return table[a[0] * 5 + (a[1] - 1) % 5] + table[b[0] * 5 + (b[1] - 1) % 5];
                } else if (a[1] == b[1]) {
                    return table[(a[0] - 1) % 5 * 5 + a[1]] + table[(b[0] - 1) % 5 * 5 + b[1]];
                } else {
                    return table[a[0] * 5 + b[1]] + table[b[0] * 5 + a[1]];
                }
            });
    };

    // 用来判断字符串前后是否重复
    String.prototype.each = function(cb) {
        var len = this.length;
        var result = '';

        for (var i = 0; i < len; i++) {
            result += cb(this[i], this[i + 1]) || this[i];
        }

        return result;
    };

    // 获取字符在密表中的位置
    var position = function(table, ch) {
        var index = table.indexOf(ch);
        return [Math.floor(index / 5), index % 5];
    };

    /* -------------------- 测试 --------------------- */
    // http://en.wikipedia.org/wiki/Playfair_cipher

    var key = 'playfair example';
    var text = 'Hide the gold in the tree stump';

    // 加密
    var ciphertext = Playfair.encrypt(key, text);
    console.log(ciphertext);

    // 解密
    console.log(Playfair.decrypt(key, ciphertext));

}());
