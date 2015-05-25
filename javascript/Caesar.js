/*
 * Caesar Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var ASCII = {
        a: 'a'.charCodeAt(),
        z: 'z'.charCodeAt(),
    };

    function caesar(words, shift) {
        return words.toLowerCase().replace(/\w/g, function(ch) {
            return getShiftCh(ch, shift);
        });
    };

    var getShiftCh = function(ch, shift) {
        var asc = ch.charCodeAt() + shift;
        var new_ch = asc;
        if (asc > ASCII.z) {
            new_ch = ((asc - ASCII.a) % 26) + ASCII.a;
        } else if (asc < ASCII.a) {
            new_ch = ASCII.z - ((ASCII.a - asc) % 26 - 1);
        }
        return String.fromCharCode(new_ch);
    };

    /* -------------------- 测试 -------------------- */

    var text = 'hello world, this is Caesar cipher.';
    var shift = 3;

    var ciphertext = caesar(text, shift);
    console.log('右移 [%s]', ciphertext);
    console.log('左移 [%s]', caesar(ciphertext, -shift));

}());
