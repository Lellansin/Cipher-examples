/*
 * ROT13 Cipher
 *
 * @author  lellansin <lellansin@gmail.com>
 * @website http://www.lellansin.com/tutorials/ciphers
 */
(function() {

    var ASCII = {
        a: 'a'.charCodeAt(),
        z: 'z'.charCodeAt(),
        A: 'A'.charCodeAt(),
        Z: 'Z'.charCodeAt(),
    };

    function rotation(words) {
        return caesar(words, 13);
    }

    function caesar(words, shift) {
        return words.replace(/([A-Z])|([a-z])/g, function(ch, upper, lower) {
            if (upper) {
                return getShiftCh(ch, ASCII.A, ASCII.Z, shift);
            }
            return getShiftCh(ch, ASCII.a, ASCII.z, shift);
        });
    }

    var getShiftCh = function(ch, start, end, shift) {
        var asc = ch.charCodeAt() + shift;
        var new_ch = asc;
        if (asc > end) {
            new_ch = ((asc - start) % 26) + start;
        } else if (asc < start) {
            new_ch = end - ((start - asc) % 26 - 1);
        }
        return String.fromCharCode(new_ch);
    };

    /* -------------------- 测试 -------------------- */

    var text = 'Gb phg bss Puvarfr fhccyvrf gb gur Abegu Xbernaf, qrfgebl obgu Fvab–Xberna Oevqtrf ol nvepensg. Sebz Abirzore 1950, hfr O-29 naq O-17 urnil obzoref, naq S-80 svtugre-obzoref gb ercrngrqyl nggnpx gur oevqtrf. -- Qbhtynf ZnpNeguhe';

    var ciphertext = rotation(text);
    console.log('解密 \n%s', ciphertext);

}());
