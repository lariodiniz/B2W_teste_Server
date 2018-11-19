#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json
from flask import request, jsonify, Blueprint, abort


from .models import Planets
from sw_server.db import db

planets = Blueprint('planets', __name__)

@planets.route("/planets/", methods=["GET"])
def list_planets():
    planetas = Planets.objects.all()
    if len(planetas) > 0:
        retorno = planetas.to_json
    else:
        retorno = []
    return jsonify(retorno)

@planets.route('/planets/', methods=['POST'])
def planet_sign():

    print(request.json)
    #planet = Planets.from_json(request.json)
    return "Cadastro"
