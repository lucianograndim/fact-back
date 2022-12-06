from os import getenv
from dotenv import load_dotenv
from flask import Flask #importamos la libreria flask


load_dotenv(".env.local")


DbConfig = {
        "host":str(getenv("BD_HOST")), #ip de la base de datos principal de xentric
        "port":str(getenv("BD_PORT")), #puerto de la base de datos principal de xentric
}

app = Flask(__name__)
app.config['DbConfig'] = DbConfig