#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from flask import request, jsonify, Blueprint

from .models import Planets
from .sw_api import SwApi

planets = Blueprint('planets', __name__)

@planets.route("/planets/", methods=["GET"])
def list_planets():
    """
    View that returns a list with all the planets registered
    :return: Json
    """
    planetas = Planets.objects.all()
    if len(planetas) > 0:
        retorno = planetas
    else:
        return jsonify({"response": "There is no planet registered."})
    return jsonify(retorno)

@planets.route('/planets/', methods=['POST'])
def planet_sign():
    """
    View that register planets
    :return: Json
    """
    data = request.get_json()

    if not data:
        return jsonify({"response": "No dictionary has been sent."})

    keys = data.keys()

    if ("name" not in keys) or ("climate" not in keys) or ("terrain" not in keys):
        return jsonify({"response": "Send only one planet for registration."})
    else:
        planet_name = data.get('name')
        if planet_name:
            planet = Planets.objects(name = planet_name)
            if planet:
                return jsonify({"response": "Planet already exists."})
            else:
                name = data['name']
                climate = data['climate']
                terrain = data['terrain']
                if 'films' not in list(data.keys()):
                    try:
                        films = SwApi().NumeroDeFilmes(name)
                    except:
                        films = 0
                else:
                    films = data['films']

                Planets(name=name, climate=climate, terrain=terrain, films=films).save()
                return jsonify({"response": "Successfully saved planet."})

@planets.route('/planets/name/<string:name>', methods=['GET'])
def get_planet_name(name):
    """
    View that returns a planets registered by the name
    :return: Json
    """
    planet = Planets.objects(name=name)
    if not planet:
        data = {"response": "The planet does not exist."}
        return jsonify(data)
    else:
        return jsonify(planet)

@planets.route('/planets/id/<id>', methods=['GET'])
def get_planet_id(id):
    """
    View that returns a planets registered by the id
    :return: Json
    """
    planet = Planets.objects(pk=id)
    if not planet:
        data = {"response": "The planet does not exist."}
        return jsonify(data)
    else:
        return jsonify(planet)

@planets.route('/planets/name/<string:name>', methods=['DELETE'])
def delete_planet_name(name):
    """
    View that delete a planets registered by the name
    :return: Json
    """

    planet = Planets.objects(name=name)
    if not planet:
        data = {"response": "The planet does not exist."}
    else:
        planet.delete()
        data = {"response": "The planet {} was removed.".format(name)}

    return jsonify(data)

@planets.route('/planets/id/<id>', methods=['DELETE'])
def delete_planet_id(id):
    """
    View that delete a planets registered by the id
    :return: Json
    """
    try:
        planet = Planets.objects(pk=id)
        if not planet:
            data = {"response": "The planet does not exist."}
        else:
            name = planet.get().name
            planet.delete()
            data = {"response": "The planet {} was removed.".format(name)}
    except:
        data = {"response": "The planet does not exist."}

    return jsonify(data)