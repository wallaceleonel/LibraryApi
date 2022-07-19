from http import server
from flask import Flask
from flask_restplus import Api , Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id':0,'title':"O conde de monte cristo"},
    {'id':1,'title':"Os tres mosqueteiros"},
    {'id':2,'title':"Alice no pais das maravilhas"}
]

@api.route('/books')
class BookList(Resource):
    def get(self,):
        return