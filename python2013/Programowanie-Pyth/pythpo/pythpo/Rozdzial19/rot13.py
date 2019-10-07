#!/usr/bin/env python

def rot13_character(character):
    # Warto�ci kod�w dla ko�c�wek alfabetu.
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')

    code = ord(character)
    # Przesuni�cie ma�ych liter.
    if a <= code <= z:
        code = a + (code - a + 13) % 26
    # Przesuniecie wielkich liter.
    elif A <= code <= Z:
        code = A + (code - A + 13) % 26
    # Pozostawienie pozosta�ych znak�w bez modyfikacji.
    else:
        pass
    return chr(code)


def rot13(plaintext):
    # Przejd� przez wszystkie litery tekstu.
    ciphertext = ""
    for character in plaintext:
        ciphertext += rot13_character(character)
    return ciphertext
