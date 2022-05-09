try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..\src'
            )
        )
    )
except:
    raise

import unittest
from src.calculadora import soma
from src.calculadora import subtrai


class TesteCalculadora(unittest.TestCase):
    #   Testando a SOMA
    def test_soma_5_e_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (-5, 5, 0),
            (1.5, 2.5, 4.0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('10', 10)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10, '10')

    #   Testando a SUBTRAÇÂO
    def test_subtrai_5_5_deve_retornar_0(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_10_negativo_e_5_deve_retornar_5(self):
        self.assertEqual(subtrai(10, 5), 5)

    def test_subtrai_varias_entradas(self):
        x_y_saidas = (
            (10, 5, 5),
            (5, 5, 0),
            (10, 8, 2),
            (-10, -5, -5),
            (1.5, 1.0, 0.5),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(subtrai(x, y), saida)

    def test_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai('5', 5)

    def test_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            subtrai(5, '3')


if __name__ == "__main__":
    unittest.main(verbosity=2)
