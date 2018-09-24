import os
from flask import Flask
import psycopg2
from consultas import Consulta

#DATABASE_URL = os.environ["postgres://atjdndhmjguhhv:9dcfd97ed53dac7246f96df9a090937f60bc12f4eba0146da001bf17420826a4@ec2-54-235-193-34.compute-1.amazonaws.com:5432/df243cki5tuf5r"]


app = Flask(__name__)

@app.route('/consultar/<identificador>')
def consultar(identificador):
	conn = psycopg2.connect(database= DATA, user= USER, password=PASS, host=HOST, port=PORT, sslmode=SSL)
	cursor = conn.cursor()
	cursor.execute("select * from users where id="+identificador)
	records = cursor.fetchall()
	return str(records)


@app.route('/cadastrar/<login>&<name>&<bio>')
def cadastrar(login, name, bio):
	Consulta().cadastrar(login, name, bio)
	return ""


@app.route('/remover/<identificador>')
def remover(identificador):
	Consulta().remover(identificador)
	return ""


@app.route('/')
def home():
	return "Hello worlaaaaad"

@app.route('/db')
def connect_db():
	return "conexao db"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
