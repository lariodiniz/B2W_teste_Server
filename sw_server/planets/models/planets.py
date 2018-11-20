#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from sw_server.db import db


class Planets(db.Document):
    """
    Model of the Planet Entity in the database.
    """

    name = db.StringField()
    climate = db.StringField()
    terrain = db.StringField()
    films = db.IntField()
