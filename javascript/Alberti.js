/*
 * Alberti cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Alberti = {};

    // 26个字母齐全
    var ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

    /*
     * 生成密表
     */
    Alberti.generateTable = function(key) {
        var table = '',
            alphabet = ALPHABET;
        key = key ? key.toUpperCase().replace(/[\W]/, '') : '';

        for (var i = 0; i < 26; i++) {
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
    Alberti.printTable = function(table) {
        console.log(table.replace(/[\w]/g, function(ch) {
            return ch + ' ';
        }));
    };

    /*
     * 加密
     */
    Alberti.encrypt = function(keys, words) {
        var table = [
            Alberti.generateTable(keys[0]),
            Alberti.generateTable(keys[1])
        ];
        var index = 0;

        return words.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return table[index++ % 2].charAt(ALPHABET.indexOf(ch));
        });
    };

    /*
     * 解密
     */
    Alberti.decrypt = function(keys, cipher) {
        var table = [
            Alberti.generateTable(keys[0]),
            Alberti.generateTable(keys[1])
        ];
        var index = 0;

        return cipher.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return ALPHABET.charAt(table[index++ % 2].indexOf(ch));
        });
    };

    /* -------------------- 测试 --------------------- */
    // 本例推算见 http://www.cryptool-online.org/index.php?option=com_cto&view=tool&Itemid=150&lang=en

    var text = 'Geheimnis';
    var keys = ['qwertzuiopasdfghjklmnbvcxy', 'plmkoijnbhuzgvcftrdxyseawq'];

    var ciphertext = Alberti.encrypt(keys, text);
    console.log('加密', ciphertext);
    console.log('解密', Alberti.decrypt(keys, ciphertext));

}());
