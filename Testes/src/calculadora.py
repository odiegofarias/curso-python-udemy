def soma(x, y):
    # """Soma x e y
    #
    # >>> soma(10, 20)
    # 30
    #
    # >>> soma(-10, 20)
    # 10
    #
    # Se quiser que o erro PASSE
    # >>> soma('10', 20)
    # Traceback (most recent call last):
    # ...
    # AssertionError: x precisa ser Int ou Float
    # """
    assert isinstance(x, (int, float)), 'x precisa ser Int ou Float'
    assert isinstance(y, (int, float)), 'y precisa ser Int ou Float'
    return x + y


def subtrai(x, y):
    # """Subtrai x e y
    #
    # >>> subtrai(10, 5)
    # 5
    # >>> subtrai(10, '10')
    # Traceback (most recent call last):
    # ...
    # AssertionError: y precisa ser Int ou Float
    # 20
    # """
    assert isinstance(x, (int, float)), 'x precisa ser Int ou Float'
    assert isinstance(y, (int, float)), 'y precisa ser Int ou Float'
    return x - y


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
