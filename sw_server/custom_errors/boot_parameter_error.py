#coding: utf-8
__author__ = "Lário dos Santos Diniz"

class BootParameterError(Exception):
    """
    Class that throws an error when the parameter passed at startup is invalid.
    """
    def __init__(self, valor):

        self.valor = valor

    def __str__(self):
        men = 'the "{}" parameter is not valid. '.format(self.valor)
        men += 'Report "development", "production" or "testing".'
        return repr(men)
