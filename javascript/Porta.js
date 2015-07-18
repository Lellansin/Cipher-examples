/*
 * Porta Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Porta = {};

    var ALPHABET = {
        "A":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]], "B":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]],
        "C":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["Z","N","O","P","Q","R","S","T","U","V","W","X","Y"]], "D":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Z","N","O","P","Q","R","S","T","U","V","W","X","Y"]],
        "E":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["Y","Z","N","O","P","Q","R","S","T","U","V","W","X"]], "F":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Y","Z","N","O","P","Q","R","S","T","U","V","W","X"]],
        "G":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["X","Y","Z","N","O","P","Q","R","S","T","U","V","W"]], "H":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["X","Y","Z","N","O","P","Q","R","S","T","U","V","W"]],
        "I":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["W","X","Y","Z","N","O","P","Q","R","S","T","U","V"]], "J":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["W","X","Y","Z","N","O","P","Q","R","S","T","U","V"]],
        "K":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["V","W","X","Y","Z","N","O","P","Q","R","S","T","U"]], "L":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["V","W","X","Y","Z","N","O","P","Q","R","S","T","U"]],
        "M":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["U","V","W","X","Y","Z","N","O","P","Q","R","S","T"]], "N":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["U","V","W","X","Y","Z","N","O","P","Q","R","S","T"]],
        "O":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["T","U","V","W","X","Y","Z","N","O","P","Q","R","S"]], "P":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["T","U","V","W","X","Y","Z","N","O","P","Q","R","S"]],
        "Q":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["S","T","U","V","W","X","Y","Z","N","O","P","Q","R"]], "R":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["S","T","U","V","W","X","Y","Z","N","O","P","Q","R"]],
        "S":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["R","S","T","U","V","W","X","Y","Z","N","O","P","Q"]], "T":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["R","S","T","U","V","W","X","Y","Z","N","O","P","Q"]],
        "U":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["Q","R","S","T","U","V","W","X","Y","Z","N","O","P"]], "V":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["Q","R","S","T","U","V","W","X","Y","Z","N","O","P"]],
        "W":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["P","Q","R","S","T","U","V","W","X","Y","Z","N","O"]], "X":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["P","Q","R","S","T","U","V","W","X","Y","Z","N","O"]],
        "Y":[["A","B","C","D","E","F","G","H","I","J","K","L","M"],
             ["O","P","Q","R","S","T","U","V","W","X","Y","Z","N"]], "Z":[["A","B","C","D","E","F","G","H","I","J","K","L","M"], ["O","P","Q","R","S","T","U","V","W","X","Y","Z","N"]]}

    /*
     * 生成密表
     */
    Porta.initTable = function(key) {
        var table = [];

        key.toUpperCase().replace(/[A-Z]/g, function(ch) {
            table.push(ALPHABET[ch]);
        });

        return table;
    };

    /*
     * 加密
     */
    Porta.encrypt = function(key, words) {
        var table = Porta.initTable(key);
        var count = 0;

        return words.toUpperCase().replace(/([A-Za-z])/g, function(ch) {
            var index = count++ % table.length;
            return getOpponent(table[index], getPosition(table[index], ch));
        });
    };

    /*
     * 解密
     */
    Porta.decrypt = function(table, text) {
        return Porta.encrypt(table, text);
    };

    // 获取字母在密表中的位置
    var getPosition = function(table, ch) {
        var col = 0;
        var pos = table[col].indexOf(ch);
        if (pos >= 0)
            return [col, pos];

        pos = table[++col].indexOf(ch);
        if (pos >= 0)
            return [col, pos];
        return null;
    };

    // 根据位置获取对应另一个字母
    var getOpponent = function(table, position) {
        if (!position[0]) {
            return table[1][position[1]];
        }
        return table[0][position[1]];
    };

    /* -------------------- 测试 -------------------- */
    // 本例推算见 http://ruffnekk.stormloader.com/Porta_info.html

    var key = 'KEY';
    var text = 'GEHEIMNIS';

    // 加密
    var ciphertext = Porta.encrypt(key, text);
    console.log('密文:', ciphertext);

    // 解密
    console.log('解密:', Porta.decrypt(key, ciphertext));

}());
