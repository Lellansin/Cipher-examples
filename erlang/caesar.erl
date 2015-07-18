%
% Caesar Cipher
% 
% @author  lellansin <lellansin@gmail.com>
% @website http://www.lellansin.com/tutorials/ciphers
%
-module(caesar).
-export([encrypt/2, decrypt/2, test/0]).

encrypt(Words, Shift) -> [ shift(C, Shift) || C <- slashes(Words) ].
decrypt(Words, Shift) -> encrypt(Words, -Shift).

% todo
slashes([]) -> [];
slashes([ H | _ ]) when H =:= "~~" -> "\\";
slashes([ H | T ]) -> [ H | slashes(T) ].

shift(C, Shift) when ((C >= $A) and (C =< $Z)) or
                     ((C >= $a) and (C =< $z)) -> 
    Offset = Shift rem 26,
    case (C >= $a) of
    	true -> 
    		if
                Offset + C > $z  ->
                     $a + (Offset + C) - $z;
                Offset + C < $a  ->
                     $z + Offset + C;
                true ->
                     C + Offset
            end;
        false -> 
            if
                Offset + C > $Z  ->
                     $A + (Offset + C) - $Z;
                Offset + C < $A  ->
                     $Z + Offset + C;
                true ->
                     C + Offset
            end
    end;
shift(C, _) -> C.

test() ->
    Text = "hello world, this is Caesar cipher.\n",
    Cipher = encrypt(Text, 3),
    io:format(Cipher),
    io:format(decrypt(Cipher, 3)).
