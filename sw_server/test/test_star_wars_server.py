#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from flask import current_app

from sw_server import StarWarsServer


class TestStarWarsServer:
    """
    Tests the StarWarsServer class
    """

    def setup(self):
        """
        Initial Test Settings
        """

        self.app = StarWarsServer("testing");
        self.client = self.app.test_client()

    def test_app_exists(self):
        """
        Checks if the application exists
        """

        assert not current_app is None

    def test_app_development_is_ok(self):
        """
        Verifies that the application does not run with the developer instance
        """

        app = StarWarsServer("development");
        assert app.mode == 'development'

    def test_app_production_is_ok(self):
        """
        Verifies that the application does not run with the production instance
        """

        app = StarWarsServer("production");
        assert app.mode == 'production'
        try:
            app = StarWarsServer("production");
            assert app.mode == 'production'
        except OSError as erro:
            test = '{} folder does not exist.'.format("production")
            assert erro.__str__() == repr(test)


    def test_app_parameter_error(self):
        """
        Checks if the application does not run with the wrong instance
        """

        try:
            app = StarWarsServer("erro");
        except Exception as erro:
            teste = 'the "erro" parameter is not valid. '
            teste += 'Report "development", "production" or "testing".'
            assert erro.__str__() == repr(teste)


    def test_mode_test(self):
        """
        Verifies that the application does not run with the test instance
        """
        assert self.app.config['ENV'] == 'testing'
        assert self.app.mode == 'testing'

    def test_index_view_status_code(self):
        """
        Checks if the index page returns the status code 200
        """
        response = self.client.get('/')

        assert response.status_code == 200

    def test_index_view_body(self):
        """
        Checks if the message "Application is working." it is in the body of the answer
        """
        response = self.client.get('/')
        assert 'Application is working.' in response.get_data(as_text=True)
