from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
	return "Hello world"

@app.route('/db')
def connect_db():
	return "conexao db"


if __name__ == "__main__":
	app.run(debug=True)
