#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from os import path
from flask import Flask, jsonify

from .custom_errors import BootParameterError
from .db import db
from .planets import planets


class StarWarsServer(Flask):

    """
    Class that inherits from the Flask class and creates the application.
    """

    def __init__(self, mode):

        self.mode = mode.lower()

        # checks the instance type and loads the specified folder
        if self.mode in ['development', 'production']:
            pasta = path.join(path.abspath(path.dirname(__file__)), "{}_instance".format(self.mode))

            if not path.exists(pasta):
                raise OSError("{} folder does not exist.".format(pasta))

        elif self.mode == 'testing':
            pasta = path.join(path.abspath(path.dirname(__file__)), "test")
        else:
            raise BootParameterError(self.mode)

        # Sets the folder of the environment being used
        instance_path = pasta

        #calls the init method of the parent class passing some initial parameters
        super(StarWarsServer, self).__init__("star_wars_server", instance_path=instance_path,
                                            instance_relative_config=True)

        #loads the environment settings
        self.config.from_pyfile('config.cfg')

        #defines the environment
        self.config['ENV'] = mode

        if self.mode == 'testing':
            self.config['TESTING'] = True

        self.register_blueprint(planets)
        db.init_app(self)


        # The initial route that informs when the application is functional
        @self.route('/')
        def hello():

            return jsonify({"response": "Application is working."})


