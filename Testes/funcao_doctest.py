# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/unittest.html
from src.calculadora import soma


# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))
# print(soma('11', 20))


try:
    print(soma('15', 20))
except AssertionError as e:
    print(f'Conta inválida. {e}')
