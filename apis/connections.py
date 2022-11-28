from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from models.Boleta import *
from models.Discrepancia import *
from models.Empresa import *
from models.Fact import *
from models.Movimiento import *
from models.OrdenCompra import *
from models.Ticket import *
from models.Users import *

application = Flask(__name__)
application.config['JSON_AS_ASCII'] = False
cors = CORS(application, resources={r"/facturacion/*": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/facturacion/client', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    #usuario = usuariodb(id)
    return jsonify(usuario)

@application.route('/facturacion/empresa/id', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    #empresa = empresa(id)
    return jsonify(empresa)

@application.route('/facturacion/client/servicios/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    #list_servicios = ServConsumdb(id)
    return jsonify(list_servicios)

@application.route('/facturacion/client/factura/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    date = request.args.get(date, type=str)
    #fact= fact_database(id,date)
    return jsonify(fact)

@application.route('/facturacion/client/boleta/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    date = request.args.get(date, type=str)
    #boleta= boleta_database(id,date)
    return jsonify(boleta)

@application.route('/facturacion/client/ticket/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    date = request.args.get(date, type=str)
    #ticket= ticket_database(id,date)
    return jsonify(ticket)

@application.route('/facturacion/client/discrepancia/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    date = request.args.get(date, type=str)
    #discrepancia= discrepancia_database(id,date)
    return jsonify(discrepancia)

@application.route('/facturacion/client/ordencompra/', methods=['GET'])
def mensaje():
    id = request.args.get(id, type=int)
    date = request.args.get(date, type=str)
    #ordencompra= ordencompra_database(id,date)
    return jsonify(ordencompra)
