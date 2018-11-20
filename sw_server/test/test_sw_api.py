#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from sw_server.planets import SwApi


class TestSWApi():

    def test_number_non_existent_planet(self):
        n = SwApi().NumeroDeFilmes('Inexistente')
        assert n == 0

    def test_number_existent_planet(self):
        n = SwApi().NumeroDeFilmes('Alderaan')
        assert n == 2

    def test_BuscarPlanetasJson(self):
        planets = SwApi().BuscarPlanetasJson()
        assert planets["count"] == 61
        assert planets["next"] == "https://swapi.co/api/planets/?page=2"
