#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from sw_server.custom_errors import BootParameterError


class TestCustomErrors():
    """
    Tests the BootParameterError class
    """

    def test_param_valor(self):
        """
        Checks if the boot parameter of the BootParameterError
        class is added in the value parameter
        """

        error = BootParameterError("teste")
        assert error.valor == "teste"

    def test_str(self):
        """
        Test if the message when throwing the exception is correct
        """

        error = BootParameterError("teste")
        test = 'the "teste" parameter is not valid. '
        test += 'Report "development", "production" or "testing".'
        assert error.__str__() == repr(test)
