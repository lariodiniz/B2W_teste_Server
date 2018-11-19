#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json


from sw_server import StarWarsServer

class TestPlanets:

    def setup(self):
        self.app = StarWarsServer("testing");
        self.client = self.app.test_client()

    def test_planets_view_get_status_code(self):
        """
        Verifica se uma requisição para a view planets retorna 200
        """
        response = self.client.get('/planets/')
        assert response.status_code == 200

    def test_planets_view_get(self):
        response = self.client.get('/planets/')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['name'] == 'Tatooine'
        assert json_response['climate'] == 'arid'
        assert json_response['terrain'] == 'desert'

