/*
 * Base64 Encoding
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var Base64 = {};
 
    var ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
 
    /*
     * 编码
     */
    Base64.encode = function (words) {
        var cipher = '', code = utf8_encode(words);
        var i = 0, chr1, chr2, chr3,
             enc1, enc2, enc3, enc4;

        while (i < code.length) {
            chr1 = code.charCodeAt(i++);
            chr2 = code.charCodeAt(i++);
            chr3 = code.charCodeAt(i++);

            enc1 = chr1 >> 2;
            enc2 = ((chr1 &  3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;

            if (isNaN(chr2))
                enc3 = enc4 = 64;
            else if (isNaN(chr3))
                enc4 = 64;

            cipher += ALPHABET.charAt(enc1) + ALPHABET.charAt(enc2) +
                      ALPHABET.charAt(enc3) + ALPHABET.charAt(enc4);
        }
        return cipher;
    };
 
    /*
     * 解码
     */
    Base64.decode = function (text) {
        var code = '', cipher = text.replace(/[^A-Za-z0-9\+\/\=]/g, '');
        var i = 0, chr1, chr2, chr3,
             enc1, enc2, enc3, enc4;

        while (i < cipher.length) {
            enc1 = ALPHABET.indexOf(cipher.charAt(i++));
            enc2 = ALPHABET.indexOf(cipher.charAt(i++));
            enc3 = ALPHABET.indexOf(cipher.charAt(i++));
            enc4 = ALPHABET.indexOf(cipher.charAt(i++));

            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;

            code += String.fromCharCode(chr1);
            if (enc3 != 64)
                code += String.fromCharCode(chr2);
            if (enc4 != 64)
                code += String.fromCharCode(chr3);
        }
        return utf8_decode(code);
    };
 
    var utf8_encode = function (string) {
        return string.replace(/([^\r])|\r/g, 
            function(text, ch) {
                if (!ch) 
                    return '';
                var c = ch.charCodeAt(0);
                if (c < 128) 
                    return ch;
                else if((c > 127) && (c < 2048))
                    return String.fromCharCode((c >> 6) | 192) + String.fromCharCode((c & 63) | 128);
                else
                    return String.fromCharCode((c >> 12) | 224) + String.fromCharCode(((c >> 6) & 63) | 128) + String.fromCharCode((c & 63) | 128);
            });
    };
 
    var utf8_decode = function (utftext) {
        var c1 = 0, c2 = 0, c3 = 0;
        return utftext.replace(/([\x0-\x7F])|([\xC0-\xDF][.])|([.]{3})/, 
            function(text, asc, ansi, utf) {
                if (asc)
                    return asc;

                c1 = text.charCodeAt(0);
                c2 = text.charCodeAt(1);

                if(ansi)
                    return String.fromCharCode(((c1 & 31) << 6) | (c2 & 63));

                c3 = utf.charCodeAt(2);
                return String.fromCharCode(((c1 & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
            });
    };

    // -------------------------------------------------

    // 明文
    var text = 'hello world!';

    // 编码
    var str = Base64.encode(text);
    console.log('密文', str); 

    // 解码
    console.log('原文', Base64.decode(str));

})();
