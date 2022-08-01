import json
from urllib import response
from flask_restful import Resource
from requests import HTTPError
import requests

from app.config import URL_BASE, TOKEN_API

class ClientCPF(Resource):
    def get(self, cpf, nascimento):
        query = {'token': TOKEN_API, 'cpf': cpf, 'data-nascimento': nascimento, 'plugin': 'CPF'}
        try:
            response = requests.get(URL_BASE, params=query).json()
            if response['status'] == "ERROR":
                return {'message': response['message']}, 404
            else:
                return {'message': response}, 200
        except HTTPError as httperr:
            return {'message': httperr}, 404
