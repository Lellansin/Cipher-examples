/*
 * Kamasutra Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Kamasutra = {};

    /*
     * 生成密表
     */
    Kamasutra.initTable = function() {
        var table = [];

        // 实际应该将26个字母随机打散生成，不过这里直接用例子里面随机的
        table[0] = 'KBJHOESNWYCVI';
        table[1] = 'APMRZQGFXDULT';

        return table;
    };

    /*
     * 打印密表
     */
    Kamasutra.printTable = function(table) {
        console.log(table[0]);
        console.log(table[1]);
    };

    /*
     * 加密
     */
    Kamasutra.encrypt = function(table, words) {
        return words.replace(/([A-Z])|([a-z])/g, function(ch, upper, lower) {
            if (lower) {
                return getOpponent(table, getPosition(table, lower.toUpperCase())).toLowerCase();
            }
            return getOpponent(table, getPosition(table, upper));
        });
    };

    /*
     * 解密
     */
    Kamasutra.decrypt = function(table, text) {
        return Kamasutra.encrypt(table, text);
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
    // 本例推算见 http://ruffnekk.stormloader.com/kamasutra_info.html

    var text = 'This is an example';

    // 生成密表 (密表就是密匙)
    var table = Kamasutra.initTable();
    Kamasutra.printTable(table);

    // 加密
    var ciphertext = Kamasutra.encrypt(table, text);
    console.log('密文:', ciphertext);

    // 解密
    console.log('解密:', Kamasutra.decrypt(table, ciphertext));

}());
