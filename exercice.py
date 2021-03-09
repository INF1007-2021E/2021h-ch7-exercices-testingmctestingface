#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle


# TODO: Définissez vos fonction ici
def f(a = 5, b = 2, c = 1, p = 4):
    V = (4/3) * math.pi * a * b * c
    M = V * p
    return (V,M)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(f())