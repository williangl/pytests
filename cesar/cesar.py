"""Cifra de Cesar."""

# biblioteca padrão
from string import ascii_lowercase

alf = ascii_lowercase


def cripto(txt: str) -> str:
    """Função de criptografia."""
    cipher = ''
    for letra in txt:
        cipher += alf[(alf.index(letra) + 3) % len(alf)]
    return cipher


def decript(txt: str) -> str:
    """Função de descriptografia."""
    plain = ''
    for letra in txt:
        plain += alf[(alf.index(letra) - 3) % len(alf)]
    return plain
