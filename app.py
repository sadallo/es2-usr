import os
from flask import Flask
import psycopg2

#DATABASE_URL = os.environ["postgres://atjdndhmjguhhv:9dcfd97ed53dac7246f96df9a090937f60bc12f4eba0146da001bf17420826a4@ec2-54-235-193-34.compute-1.amazonaws.com:5432/df243cki5tuf5r"]

USER="atjdndhmjguhhv"
PASS="9dcfd97ed53dac7246f96df9a090937f60bc12f4eba0146da001bf17420826a4"
HOST="http://ec2-54-235-193-34.compute-1.amazonaws.com"
PORT=5432
DATA="df243cki5tuf5r"
SSL="require"

app = Flask(__name__)

@app.route('/conn')
def consulta():
	conn = psycopg2.connect(database= DATA, user= USER, password=PASS, host=HOST, port=PORT, sslmode=SSL)
	#conn = psycopg2.connect(DATABASE_URL, sslmode="require")
	'''cursor = conn.cursor()
	cursor.execute("select * from estado where uf = '"+arg.upper()+"'")
	records = cursor.fetchall()
	if len(records) == 0:
		return "NAo existe um estado com a sigla "+str(arg)
	return ""+records[0][1]+" - "+records[0][0]'''
	if 1:
		return "conectado";
@app.route('/')
def home():
	return "Hello world"

@app.route('/db')
def connect_db():
	return "conexao db"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)