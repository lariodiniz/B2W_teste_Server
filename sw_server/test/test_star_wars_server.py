#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import re
from flask import current_app


from sw_server import StarWarsServer


class TestStarWarsServer:

    def setup(self):
        self.app = StarWarsServer("testing");
        self.client = self.app.test_client()

    def test_app_exists(self):
        """
        Verifica se a aplicação existe
        """
        assert not current_app is None

    def test_mode_test(self):
        """
        Verifica se a aplicação esta em modo teste.
        """
        assert  self.app.config['ENV'] == 'testing'

    def test_index_view_status_code(self):
        """
        Verifica se a pagina index retorna o status code 200
        """
        response = self.client.get('/')

        assert response.status_code == 200

    def test_index_view_body(self):
        """
        Verifica se a mensagem "Application is working." esta no corpo da resposta.
        """
        response = self.client.get('/')
        assert 'Application is working.' in response.get_data(as_text=True)





