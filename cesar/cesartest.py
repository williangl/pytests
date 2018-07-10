"""Teste cifra de Cesar."""

# biblioteca padrão
from unittest import TestCase, main

# minha biblioteca
import cesar


class TesteCesar(TestCase):
    """Classe de teste."""

    def test_cripto(self):
        """Testar a função de criptografia."""
        entrada = 'abc'
        esperado = 'def'
        self.assertEqual(cesar.cripto(entrada), esperado)

    def test_xyz(self):
        """Testar criptografia com as últimas letras do alfabeto."""
        entrada = 'xyz'
        esperado = 'abc'
        self.assertEqual(cesar.cripto(entrada), esperado)

    def test_decript(self):
        """Testar a função de descriptografia."""
        entrada = 'def'
        esperado = 'abc'
        self.assertEqual(cesar.decript(entrada), esperado)


main()
