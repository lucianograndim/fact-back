from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import environ

app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
mongo = PyMongo(app)
db = mongo.db

# ----------Collections----------
# db_user = db['user']
# db_admin = db['admin']
# db_admin_fact = db['admin_factura']
# db_admin_user = db['admin_usuarios']
# db_mod_user = db['modificar_user']
# db_fact_cli = db['factura_cliente']
# db_enterprise = db['empresa']
# db_support = db['soporte']
# doc_type = db['tipo_documento']
# div_type = db['tipo_documento']
# state_type = db['tipo_documento']
# rol_type = db['tipo_documento']
# ----------Collections----------




@app.route('/api/todo/<todo_id>', methods=['GET'])
def getTodo(todo_id):
    _todo = db.todo.find_one({"_id": ObjectId(todo_id)})
    item = {
        'id': str(_todo['_id']),
        'todo': _todo['todo']
    }

    return jsonify(data=item), 200


@app.route('/api/todo', methods=['GET'])
def getTodos():
    _todos = db.todo.find()
    item = {}
    data = []
    for todo in _todos:
        item = {
            'id': str(todo['_id']),
            'todo': todo['todo']
        }
        data.append(item)

    return jsonify(data=data), 200


@app.route('/api/todo', methods=['POST'])
def createTodo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(data=data), 201


@app.route('/api/todo/<todo_id>', methods=['PATCH'])
def updateTodo(todo_id):
    data = request.get_json(force=True)
    db.todo.update_one({"_id": ObjectId(todo_id)}, {"$set": data})

    return jsonify(data=data), 204


@app.route('/api/todo/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    db.todo.delete_one({"_id": ObjectId(todo_id)})

    return jsonify(), 204


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)






