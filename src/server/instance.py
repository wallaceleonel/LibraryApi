from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Library Book API',
            description= 'Api library',
            doc='/docs'
        )

    def run(self,):
        self.app.run(
            debug=True
        )

server = Server()