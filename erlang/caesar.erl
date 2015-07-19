%
% Caesar Cipher
% 
% @author  lellansin <lellansin@gmail.com>
% @website http://www.lellansin.com/tutorials/ciphers
%
-module(caesar).
-export([encrypt/2, decrypt/2, test/0]).

% 
% 加密
% 
encrypt(Words, Shift) -> [ shift(C, Shift) || C <- slashes(Words) ].

% 
% 解密
% 
decrypt(Words, Shift) -> encrypt(Words, -Shift).

% 
% 转义
% 
slashes(Words) ->
    re:replace(Words, "~n", "\n", [ global, { return, list } ]).

% 
% 位移
% 
shift(C, Shift) when ((C >= $A) and (C =< $Z)) ->
    Offset = Shift rem 26,
    if
        Offset + C > $Z  -> $A + (Offset + C) - $Z;
        Offset + C < $A  -> $Z + Offset + C;
        true -> C + Offset
    end;
shift(C, Shift) when ((C >= $a) and (C =< $z)) ->
    Offset = Shift rem 26,
	if
        Offset + C > $z  -> $a + (Offset + C) - $z;
        Offset + C < $a  -> $z + Offset + C;
        true -> C + Offset
    end;
shift(C, _) -> C.

% 
% 测试
% 
test() ->
    Text = "hello world, this is Caesar cipher.~n",
    Cipher = encrypt(Text, 3),
    io:format(Cipher),
    io:format(decrypt(Cipher, 3)).
