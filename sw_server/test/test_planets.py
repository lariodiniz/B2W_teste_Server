#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json

from sw_server import StarWarsServer
from sw_server.planets.models import Planets


class TestPlanets():
    """
    Tests the BootParameterError class
    """

    def setup(self):
        self.app = StarWarsServer("testing");
        self.client = self.app.test_client()

    def _apagaTodosOsPlanetas(self):
        """
        Delete all planets from the database.
        """
        planets = Planets.objects.all()
        for planet in planets:
            planet.delete()

    def test_planets_view_get_status_code(self):
        """
        Checks if a request for view planets returns 200
        """
        response = self.client.get('/planets/')
        assert response.status_code == 200

    def test_planets_view_get_without_planets(self):
        """
        Checks if a request for the view planets when there is no planets registered returns
        the message: There is no planet registered.
        """
        self._apagaTodosOsPlanetas()
        response = self.client.get('/planets/')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'There is no planet registered.'

    def test_planets_view_get_with_planets(self):
        """
        Checks if a request for the view planets when there are registered planets returns
        planets.
        """
        self._apagaTodosOsPlanetas()
        Planets(name="testeName", climate="testeClimate", terrain="testeTerrain", films=0).save()
        response = self.client.get('/planets/')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response[0]['name'] == 'testeName'
        assert json_response[0]['climate'] == 'testeClimate'
        assert json_response[0]['terrain'] == 'testeTerrain'
        assert json_response[0]['films'] == 0

    def test_get_planets_for_name(self):
        """
        Checks if a request gets to the turn planet/name/PlaneName
        returns the specific planet.
        """
        self._apagaTodosOsPlanetas()
        Planets(name="testeForName", climate="testeClimate", terrain="testeTerrain", films=0).save()
        Planets(name="teste", climate="teste", terrain="teste", films=0).save()
        response = self.client.get('/planets/name/testeForName')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response[0]['name'] == 'testeForName'
        assert json_response[0]['climate'] == 'testeClimate'
        assert json_response[0]['terrain'] == 'testeTerrain'
        assert json_response[0]['films'] == 0

    def test_get_planets_not_exist_for_name(self):
        """
        Checks if a request for the view planet/name/PlaneName when there is no planets registered returns
        the message: The planet does not exist.
        """
        self._apagaTodosOsPlanetas()

        response = self.client.get('/planets/name/testeForName')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response['response'] == 'The planet does not exist.'

    def test_get_planets_not_exist_for_id(self):
        """
        Checks if a request for the view planet/id/PlaneId when there is no planets registered returns
        the message: The planet does not exist.
        """
        self._apagaTodosOsPlanetas()

        response = self.client.get('/planets/id/5bf43a5695e0bd1dc4caad4a')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'The planet does not exist.'


    def test_get_planets_for_id(self):
        """
        Checks if a request gets to the turn planet/id/PlaneId
        returns the specific planet.
        """
        self._apagaTodosOsPlanetas()
        Planets(name="testeForId", climate="testeClimate", terrain="testeTerrain", films=0).save()
        id = Planets.objects.get_or_404(name='testeForId').id
        response = self.client.get('/planets/id/{}'.format(id))
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response[0]['name'] == 'testeForId'
        assert json_response[0]['climate'] == 'testeClimate'
        assert json_response[0]['terrain'] == 'testeTerrain'
        assert json_response[0]['films'] == 0

    def test_delete_planets_for_id(self):
        """
        Checks if a delete request for the planet/id/PlaneId view deletes specific planet
        """
        self._apagaTodosOsPlanetas()
        Planets(name="testeDeleteForId", climate="testeClimate", terrain="testeTerrain", films=0).save()
        id = Planets.objects.get_or_404(name='testeDeleteForId').id
        response = self.client.delete('/planets/id/{}'.format(id))
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'The planet testeDeleteForId was removed.'

        planet = Planets.objects(name="testeDeleteForId").first()
        assert planet == None

    def test_delete_not_exist_planets_for_id(self):
        """
        Checks if a delete request for the view planet/id/PlaneId when there is no planets registered returns
        the message: The planet does not exist.
        """
        self._apagaTodosOsPlanetas()

        response = self.client.delete('/planets/id/5bf43a5695e0bd1dc4caad4a')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'The planet does not exist.'

    def test_delete_planets_for_name(self):
        """
        Checks if a delete request for the planet/name/PlaneName view deletes specific planet
        """
        self._apagaTodosOsPlanetas()
        Planets(name="testeDeleteForName", climate="testeClimate", terrain="testeTerrain", films=0).save()
        response = self.client.delete('/planets/name/testeDeleteForName')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'The planet testeDeleteForName was removed.'

        planet = Planets.objects(name="testeDeleteForName").first()
        assert planet == None

    def test_delete_not_exist_planets_for_name(self):
        """
        Checks if a delete request for the view planet/name/PlanePlane when there is no planets registered returns
        the message: The planet does not exist.
        """
        self._apagaTodosOsPlanetas()

        response = self.client.delete('/planets/name/testeDeleteForName')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'The planet does not exist.'


    def test_planets_view_post_without_data(self):
        """
        Checks is a post request for view planets without json returns
        the message: No dictionary has been sent.
        """

        self._apagaTodosOsPlanetas()

        response = self.client.post('/planets/', data=json.dumps({}),content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'No dictionary has been sent.'

    def test_planets_view_post_data_paramet_erro(self):
        """
        Checks is a post request for view planets wrong json returns
        the message: Send only one planet for registration.
        """

        self._apagaTodosOsPlanetas()

        planeta = {'nome': "testeName", "clima":"testeClimate", "terrain": "testeTerrain", "films":0}

        response = self.client.post('/planets/', data=json.dumps(planeta),content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))
        assert json_response['response'] == 'Send only one planet for registration.'

    def test_planets_view_post_data_paramet_ok(self):
        """
        Checks is a post request for view planets correct json returns
        the message: Successfully saved planet. and save planet in the database.
        """

        self._apagaTodosOsPlanetas()

        planeta = {'name': "testeName", "climate":"testeClimate", "terrain": "testeTerrain", "films":0}

        response = self.client.post('/planets/', data=json.dumps(planeta),content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response['response'] == 'Successfully saved planet.'

        planet = Planets.objects.get_or_404(name='testeName')
        assert planeta['name'] == planet.name
        assert planeta['climate'] == planet.climate
        assert planeta['terrain'] == planet.terrain
        assert planeta['films'] == planet.films

    def test_planets_view_post_planet_exist(self):
        """
        Verifica se uma requisição via post para a view planets valida requisições
        sem json.
        """

        self._apagaTodosOsPlanetas()

        planeta = {'name': "testeName", "climate":"testeClimate", "terrain": "testeTerrain"}

        Planets(name="testeName", climate="testeClimate", terrain="testeTerrain", films=0).save()

        response = self.client.post('/planets/', data=json.dumps(planeta), content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response['response'] == 'Planet already exists.'

    def test_planets_view_post_data_paramet_without_films(self):
        """
        Checks is a post request for view planets correct json without films number
        the message: Successfully saved planet. and save planet in the database.
        """

        self._apagaTodosOsPlanetas()

        planeta = {'name': "testeName", "climate":"testeClimate", "terrain": "testeTerrain"}
        planeta2 = {'name': "Alderaan", "climate": "temperate", "terrain": "grasslands, mountains"}

        response = self.client.post('/planets/', data=json.dumps(planeta),content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response['response'] == 'Successfully saved planet.'

        planet = Planets.objects.get_or_404(name='testeName')
        assert planeta['name'] == planet.name
        assert planeta['climate'] == planet.climate
        assert planeta['terrain'] == planet.terrain
        assert 0 == planet.films

        response = self.client.post('/planets/', data=json.dumps(planeta2),content_type='application/json')
        json_response = json.loads(response.get_data(as_text=True))

        assert json_response['response'] == 'Successfully saved planet.'

        planet = Planets.objects.get_or_404(name='Alderaan')
        assert planeta2['name'] == planet.name
        assert planeta2['climate'] == planet.climate
        assert planeta2['terrain'] == planet.terrain
        assert 2 == planet.films
