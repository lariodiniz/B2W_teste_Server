from sw_server import StarWarsServer
import json

class TestStarWarsServer:

    def setup(self):
        self.app = StarWarsServer("testing");
        self.client = self.app.test_client()

    def test_mode_test(self):
        """
        Verifica se a aplicação esta em modo teste.
        """
        assert self.app.config['ENV'] == 'testing'

    def test_index_view_status_code(self):
        """
        Verifica se a pagina index retorna o status code 200
        """
        response = self.client.get('/')

        assert response.status_code == 200



