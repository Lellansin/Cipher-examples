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
     * 加密
     */
    Vigenere.encrypt = function(key, words) {
        var table = Vigenere.initTable();
        var count = 0;
        key = key.toUpperCase();
        return words.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return table[key[count++ % key.length].charCodeAt() - ASCII.A][ch.charCodeAt() - ASCII.A];
        });
    };

    /*
     * 解密
     */
    Vigenere.decrypt = function(key, text) {
        var count = 0;
        key = key.toUpperCase();
        return text.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(match, ch) {
            var offset = ch.charCodeAt() - key[count++ % key.length].charCodeAt();
            offset >= 0 ? null : offset += TABLE_WIDTH;
            return String.fromCharCode(ASCII.A + offset);
        });
    };

    /* -------------------- 测试 -------------------- */
    // 本例推算见《密码学基础》(西安电子科技大学出版社) 第5页

    var text = "block cipher design principles";
    var key = "computer";
    var ciphertext;

    // 加密
    var ciphertext = Vigenere.encrypt(key, text);
    console.log(ciphertext);

    // 解密
    console.log(Vigenere.decrypt(key, ciphertext));

}());
