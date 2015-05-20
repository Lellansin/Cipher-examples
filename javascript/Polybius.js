/*
 * Polybius Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Polybius = {};

    /*
     * 生成棋盘
     */
    Polybius.generateTable = function() {
        var alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
        var table = '';
        var rand;

        while (alphabet.length) {
            rand = alphabet[random(0, alphabet.length)];
            alphabet = alphabet.replace(rand, '');
            table += rand;
        }

        return table;
    };

    /*
     * 打印棋盘
     */
    Polybius.printTable = function(table) {
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
    Polybius.encrypt = function(table, text) {
        var cipher = '';
        text = text.toUpperCase().replace(/J/g, 'I');

        for (var i = 0; i < text.length; i++) {
            var index = table.indexOf(text[i]);
            if (index >= 0) {
                cipher += (Math.floor(index / 5) + 1) * 10 + (index % 5 + 1);
            }
        }
        return cipher;
    };

    /*
     * 解密
     */
    Polybius.decrypt = function(table, numbers) {
        var result = '';
        var array = numbers.replace(/\s/, '').match(/\d\d/g);

        for (var i = 0; i < array.length; i++) {
            var pos = array[i];
            var y = pos[0] - 1;
            var x = pos[1] - 1;
            result += table[y * 5 + x];
        }

        return result;
    };

    var random = function(min, max) {
        return min + Math.floor(Math.random() * (max - min));
    };

    /* -------------------- 测试 --------------------- */

    var text = 'hello world, this is a encrypt/decrypt test!';

    // 生成棋盘
    var table = Polybius.generateTable();
    Polybius.printTable(table);

    // 加密
    var ciphertext = Polybius.encrypt(table, text);
    console.log(ciphertext);

    // 解密
    console.log(Polybius.decrypt(table, ciphertext));

}());
