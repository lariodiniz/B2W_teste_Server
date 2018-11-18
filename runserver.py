#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import sys

from sw_server import StarWarsServer


mode = sys.argv[1] if len(sys.argv) > 1 else 'development'


# creates an instance of the application.
app = StarWarsServer(mode)
app.run(**app.config.get_namespace('RUN_'))







