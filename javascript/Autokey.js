/*
 * Autokey Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Autokey = {};

    var TABLE_WIDTH = 26;
    var ASCII = {
        A: 'A'.charCodeAt()
    };

    /*
     * 生成密表
     */
    Autokey.initTable = function() {
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
    Autokey.encrypt = function(key, words) {
        var table = Autokey.initTable();
        var count = 0;
        return words.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return table[key[count++ % key.length].charCodeAt() - ASCII.A][ch.charCodeAt() - ASCII.A];
        });
    };

    /*
     * 解密
     */
    Autokey.decrypt = function(key, text) {
        var count = 0;
        return text.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(match, ch) {
            var offset = ch.charCodeAt() - key[count++ % key.length].charCodeAt();
            if (offset < 0) offset += TABLE_WIDTH;
            return String.fromCharCode(ASCII.A + offset);
        });
    };

    // 获取密匙
    var getKey = function(words, keyword) {
        if (!keyword)
            return words.replace(/[\W]/g, '').toUpperCase();

        if (keyword.length < words.length)
            return (keyword + words.replace(/[\W]/g, '').substr(0, words.length - keyword.length)).toUpperCase();

        return keyword.toUpperCase();
    };

    /* -------------------- 测试 -------------------- */
    // 本例推算见 http://www.cryptool-online.org/index.php?option=com_content&view=article&id=104&Itemid=127&lang=en

    var text = 'THIS IS A SECRET TEXT';
    var keyword = 'KEY';

    // 密匙
    var key = getKey(text, keyword);
    console.log(key);

    // 加密
    var ciphertext = Autokey.encrypt(key, text);
    console.log(ciphertext);

    // 解密
    console.log(Autokey.decrypt(key, ciphertext));

}());
