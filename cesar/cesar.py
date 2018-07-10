"""Cifra de Cesar."""

# biblioteca padrão
from string import ascii_lowercase

alf = ascii_lowercase

txt1 = 'abc'
txt2 = 'xyz'


def cripto(txt1: str) -> str:
    """Função de criptografia."""
    cipher1 = ''
    for letra1 in txt1:
        cipher1 += alf[(alf.index(letra1) + 3) % len(alf)]
    return cipher1


"""
def xyz(txt: str) -> str:

    cipher2 = []
    for letra2 in txt2:
        cipher2.append(alf[(alf.index(letra2) + 3) % len(alf)])
    return ''.join(cipher2)
    return ''.join(cipher2)
"""
