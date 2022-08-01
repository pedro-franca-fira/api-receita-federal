
import json
from flask_restful import Resource
import pandas as pd
from app.models import Upload

class CertidaoCPF(Resource):


    def post(self, cpf):
        data_df = {'CPF_CNPJ': cpf, 'TIPO': 'PF', 'STATUS': 1, 'TENTATIVAS': 0}
        data = pd.DataFrame([data_df])

        status = Upload.execute(data, "ConsultaCertidaoRequisicao")
        return {'status_code': status[0], 'message': status[1]}, status[0]

class CertidaoCNPJ(Resource):

    def post(self, cnpj):
        data_df = {'CPF_CNPJ': cnpj, 'TIPO': 'PJ', 'STATUS': 1, 'TENTATIVAS': 0}
        data = pd.DataFrame([data_df])
        status = Upload.execute(data, "ConsultaCertidaoRequisicao")
        return {'status_code': status[0], 'message': status[1]}, status[0]

