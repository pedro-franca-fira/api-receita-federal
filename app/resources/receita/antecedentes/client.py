import json
from flask_restful import Resource
import pandas as pd
from app.models import Upload

class ClientPFNome(Resource):


    def post(self, nome):
        data_df = {'NOME': nome, 'STATUS': 1, 'TENTATIVAS': 0}
        data = pd.DataFrame([data_df])

        status = Upload.execute(data, 'ConsultaPFRequisicao')
        return {'status_code': status[0], 'message': status[1]}, status[0]

class ClientPFDocument(Resource):

    def post(self, nome, document):
        data_df = {'NOME': nome, 'CPF': document, 'STATUS': 1, 'TENTATIVAS': 0}
        data = pd.DataFrame([data_df])
        status = Upload.execute(data, 'ConsultaPFRequisicao')
        return {'status_code': status[0], 'message': status[1]}, status[0]

