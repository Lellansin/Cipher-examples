/*
 * Vigenere Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Vigenere = {};

    var TABLE_WIDTH = 26;
    var ASCII = {
        A: 'A'.charCodeAt()
    };

    /*
     * 生成密表
     */
    Vigenere.initTable = function() {
        var table = [];

        for (var i = 0; i < TABLE_WIDTH; i++) {
            var line = [];
            for (var j = 0; j < TABLE_WIDTH; j++) {
                line[j] = String.fromCharCode(ASCII.A + (i + j) % TABLE_WIDTH);
            }
            table.push(line);
        }

        return table;
    };

    /*
     * 打印密表
     */
    Vigenere.printTable = function(table) {
        var str = '';
        for (var i = 0; i < TABLE_WIDTH; i++) {
            for (var j = 0; j < TABLE_WIDTH; j++) {
                str += table[i][j] + ' '
            }
            str += '\n'
        }
        console.log(str);
    };

    /*
     * 加密
     */
    Vigenere.encrypt = function(table, key, words) {
        var count = 0;
        key = key.toUpperCase();
        words = words.toUpperCase();
        return words.replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return table[key[count++ % key.length].charCodeAt() - ASCII.A][ch.charCodeAt() - ASCII.A];
        });
    };

    /*
     * 解密
     */
    Vigenere.decrypt = function(table, key, text) {
        var count = 0;
        key = key.toUpperCase();
        text = text.toUpperCase();
        return text.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            var offset = ch.charCodeAt() - key[count++ % key.length].charCodeAt();
            offset >= 0 ? null : offset += TABLE_WIDTH;
            return String.fromCharCode(ASCII.A + offset).toLowerCase();
        });
    };

    /* -------------------- 测试 -------------------- */

    var secret = "computer";
    var text = "block cipher design principles";
    var ciphertext;

    // 生成密表
    var table = Vigenere.initTable();
    Vigenere.printTable(table);

    // 加密
    var ciphertext = Vigenere.encrypt(table, secret, text);
    console.log(ciphertext);

    // 解密
    console.log(Vigenere.decrypt(table, secret, ciphertext));

}());
