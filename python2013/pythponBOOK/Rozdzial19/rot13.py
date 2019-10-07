#!/usr/bin/env python

def rot13_character(character):
    # Warto¶ci kodów dla koñcówek alfabetu.
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')

    code = ord(character)
    # Przesuniêcie ma³ych liter.
    if a <= code <= z:
        code = a + (code - a + 13) % 26
    # Przesuniecie wielkich liter.
    elif A <= code <= Z:
        code = A + (code - A + 13) % 26
    # Pozostawienie pozosta³ych znaków bez modyfikacji.
    else:
        pass
    return chr(code)


def rot13(plaintext):
    # Przejd¼ przez wszystkie litery tekstu.
    ciphertext = ""
    for character in plaintext:
        ciphertext += rot13_character(character)
    return ciphertext
