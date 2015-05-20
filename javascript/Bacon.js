/*
 * Bacon's cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Bacon = {};

    var A = 'A'.charCodeAt();

    /*
     * 生成培根字典
     */
    Bacon.generateDict = function() {
        var dict = {};
        for (var i = 0; i < 26; i++) {
            dict[getKey(i + 1)] = String.fromCharCode(A + i);
        }
        return dict;
    };

    var getKey = function(num) {
        var bin = num.toString(2);
        var tmp = '';

        for (var i = 4; i >= 0; i--)
            if (bin[i] === undefined)
                tmp += '0';
            else
                break;

        if (tmp)
            bin = tmp + bin;

        return bin.replace(/\d/g, function(n) {
            if (n == '1') return 'B';
            else return 'A';
        });
    };

    /*
     * 加密
     */
    Bacon.encrypt = function(dict, words) {
        return words.toUpperCase().replace(/[\W]*(\w)[\W]*/g, function(text, ch) {
            return getKey(ch.charCodeAt() - A + 1);
        });
    };

    /*
     * 解密
     */
    Bacon.decrypt = function(dict, words) {
        return words.toUpperCase().replace(/[AB]{5}/g, function(key) {
            return dict[key];
        });
    };

    /* -------------------- 测试 --------------------- */

    var text = 'hello world';
    var dict = Bacon.generateDict();

    var ciphertext = Bacon.encrypt(dict, text);
    console.log('加密', ciphertext);
    console.log('解密', Bacon.decrypt(dict, ciphertext));

}());
