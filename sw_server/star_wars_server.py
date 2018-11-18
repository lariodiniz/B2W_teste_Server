from os import path
from flask import Flask

from .custom_errors import BootParameterError

#from .blueprints.noticias import noticicas_blueprint
#from .db import db

class StarWarsServer(Flask):

    """
    Class that inherits from the Flask class and creates the application.
    """

    def __init__(self, mode):

        self.mode = mode.lower()

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

        if self.mode in ['development', 'production']:
            #sets the folder where the media files will be
            self.config['MEDIA_ROOT'] = path.join(
                path.dirname(__file__),
                self.instance_path,
                self.config.get('MEDIA_FOLDER')
            )

        #defines the environment
        self.config['ENV'] = mode

        if self.mode == 'testing':
            self.config['TESTING'] = True

        # app.register_blueprint(noticicas_blueprint)

        # Bootstrap(app)
        # db.init_app(app)

        # The initial route that informs when the application is functional
        @self.route('/')
        def hello():
            return 'Application is working.'

