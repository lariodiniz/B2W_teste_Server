#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import requests
from .models import Planets

class SwApi():

    """
    Class that communicates with the api https://swapi.co
    """
    def __get(self, buscar, secundario = ""):
        """
        Makes a request for api
        :param buscar: plants, people,  starships
        :param secundario: Id
        :return: request object
        """
        return requests.get('https://swapi.co/api/{}/{}'.format(buscar, secundario))

    def BuscarPlanetasJson(self):
        """
        Search for planets in Api
        :return: Json
        """
        return self.__get('planets').json()

    def NumeroDeFilmes(self, name):
        """
        Search for the number of movies the planet appears on Api
        :param name: name of the planet
        :return: int
        """
        filme = 0
        link = 'https://swapi.co/api/planets/?page=1'
        while (link) and (filme == 0):
            busca = requests.get(link).json()
            planeta = [nam for nam in busca['results'] if nam['name'] == name]
            filme = len(planeta[0]['films']) if len(planeta) > 0 else 0
            link = busca['next']

        return filme
