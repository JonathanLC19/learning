import requests
from datetime import datetime


def listerizar(lista):
    """ Corrige el formato de listas interiores de webhook de Spread """

    new = []

    for i in lista:
        each = i[0]
        new.append(each)
        print(each)

    return new