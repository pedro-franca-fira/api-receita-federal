from flask import Flask
from flask_restful import Api

from app.resources.receita.cnpj.client import ClientCNPJ
from app.resources.receita.cpf.client import ClientCPF
from app.resources.receita.antecedentes import ClientPFNome, ClientPFDocument
from app.resources.receita.certidao import CertidaoCNPJ, CertidaoCPF

app = Flask(__name__)
api = Api(app)

api.add_resource(ClientCNPJ, '/consulta/cnpj/<string:cnpj>/token/<string:token>')
api.add_resource(ClientCPF, '/consulta/cpf/<string:cpf>/<string:nascimento>/token/<string:token>')
api.add_resource(ClientPFNome, '/consulta/nome/<string:nome>')
api.add_resource(ClientPFDocument, '/consulta/nome/<string:nome>/cpf/<string:document>')
api.add_resource(CertidaoCPF, '/consultaCertidao/cpf/<string:cpf>')
api.add_resource(CertidaoCNPJ, '/consultaCertidao/cnpj/<string:cnpj>')


if __name__ == '__main__':
        app.run(debug=True)
