/*
 *MorseCode
 *
 *@authorlellansin<lellansin@gmail.com>
 *@websitehttp://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Morse = {};

    //加密表
    var entable = {
        'a': '.- ',
        'b': '-... ',
        'c': '-.-. ',
        'd': '-.. ',
        'e': '. ',
        'f': '..-. ',
        'g': '--. ',
        'h': '.... ',
        'i': '.. ',
        'j': '.--- ',
        'k': '-.- ',
        'l': '.-.. ',
        'm': '-- ',
        'n': '-. ',
        'o': '--- ',
        'p': '.--. ',
        'q': '--.- ',
        'r': '.-. ',
        's': '... ',
        't': '- ',
        'u': '..- ',
        'v': '...- ',
        'w': '.-- ',
        'x': '-..- ',
        'y': '-.-- ',
        'z': '--.. ',
        '0': '----- ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        ' ': '/ ',
        ',': '--..--  ',
        '.': '._._._ ',
        ',': '__..__ ',
        '?': '..__.. ',
        '\'': '.____. ',
        '/': '_.._. ',
        '(': '_.__. ',
        ')': '_.__._ ',
        '&': '._... ',
        ':': '___... ',
        ';': '_._._. ',
        '=': '_..._ ',
        '+': '._._. ',
        '-': '_...._ ',
        '_': '..__._ ',
        '\\': '._.._. ',
        '$': '..._.._ ',
        '!': '_._.__ ',
        '@': '.__._. '
    };

    //解密表
    var detable = (function(code) {
        var table = {};
        for (var key in code) {
            table[code[key]] = key;
        }
        return table;
    })(entable);

    /*
     *编码
     */
    Morse.encode = function(text) {
        return text
            .toLowerCase()
            .replace(/[\w\W]/g, function(ch) {
                return entable[ch] || '';
            })
    };

    /*
     *解码
     */
    Morse.decode = function(cipher) {
        var text = ''
        cipher = cipher.toLowerCase();
        for (var cur = 0, i = 1; i <= cipher.length; i++) {
            var key = cipher.substring(cur, i);
            var str = detable[key];
            if (str) {
                text += str;
                cur = i;
            }
        }
        return text;
    };

    /*--------------------测试---------------------*/
    // http://morsecode.scphillips.com/translator.html

    //明文
    var text = '.-- .... . -. / .. / ..- ... . / .- / .-- --- .-. -.. __..__ / .. - / -- . .- -. ... / .--- ..- ... - / .-- .... .- - / .. / -.-. .... --- --- ... . / .. - / - --- / -- . .- -. / _...._ _...._ / -. . .. - .... . .-. / -- --- .-. . / -. --- .-. / .-.. . ... ... ._._._ ';

    //解密
    var plaintext = Morse.decode(text);
    console.log(plaintext);

    //加密
    var ciphertext = Morse.encode(plaintext);
    console.log('it\'', ciphertext == text);

}());
