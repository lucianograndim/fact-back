from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Resource
from bson.json_util import dumps

from models.Boleta import *
from models.Discrepancia import *
from models.Empresa import *
from models.Fact import *
from models.Movimiento import *
from models.OrdenCompra import *
from models.Ticket import *
from models.Users import *
from utils.DataBase import *
from utils.CreateFact import *
from bson.objectid import ObjectId


# application = Flask(__name__)
# application.config['JSON_AS_ASCII'] = False
# cors = CORS(application, resources={r"/facturacion/*": {"origins": "*"}})
# application.config['CORS_HEADERS'] = 'Content-Type'

# @application.route('/facturacion/client', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=int)
#     a={'_id': ObjectId(id)}
#     mesj=get("usuario",a)
#     return jsonify(mesj)


# @application.route('/facturacion/empresa/id', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     a={'_id': ObjectId(id)}
#     mesj=get("empresa",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/servicios/detalle', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     end= request.args.get(end, type=str)
#     start= request.args.get(start, type=str)
#     a={'user_id': ObjectId(id), 'fechaUP': {'$lt': end, '$gte': start}}
#     mesj=get("movimiento",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/factura/', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     date = request.args.get(date, type=str)
#     a= {'user_id': ObjectId(id), 'fecha_fac': date}
#     mesj=get("Fact",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/boleta/', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     date = request.args.get(date, type=str)
#     a= {'user_id': ObjectId(id), 'fecha_bol': date}
#     mesj=get("boleta",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/ticket/', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     date = request.args.get(date, type=str)
#     a= {'user_id': ObjectId(id), 'fechaUP': date}
#     mesj=get("ticket",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/discrepancia/', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     date = request.args.get(date, type=str)
#     a= {'user_id': ObjectId(id), 'fecha_dis': date}
#     mesj=get("discrepancia",a)
#     return jsonify(mesj)

# @application.route('/facturacion/client/ordencompra/', methods=['GET'])
# def mensaje():
#     id = request.args.get(id, type=str)
#     date = request.args.get(date, type=str)
#     a= {'user_id': ObjectId(id), 'fecha_oc': date}
#     mesj=get("ordencompra",a)
#     return jsonify(mesj)

class EndPoint3(Resource):
    
    def get(self):
        mydb = g.db
        qry = {"client": session["user"]["bdName"]}
        data = mydb["info"].find(qry)
        return dumps(data), 2006