import psycopg2


USER="atjdndhmjguhhv"
PASS="9dcfd97ed53dac7246f96df9a090937f60bc12f4eba0146da001bf17420826a4"
HOST="ec2-54-235-193-34.compute-1.amazonaws.com"
PORT=5432
DATA="df243cki5tuf5r"
SSL="require"


class Consulta:
	def __init__(self):
		self.conn = psycopg2.connect(database=DATA, user=USER, password=PASS, host=HOST, port=PORT, sslmode=SSL)			

	def cadastrar(self, login, name, bio):
		cursor = self.conn.cursor()
		sql = "insert into users (login, name, bio) values (%s, %s, %s)"
		val = (login, name, bio)
		cursor.execute(sql, val)
		self.conn.commit()
		
	def remover(self, identificador):
		cursor = self.conn.cursor()
		sql = "delete from users where id = %s"
		val = (str(identificador))
		cursor.execute(sql, val)
		self.conn.commit()

	def seguir(self, follower, followed):
		cursor = self.conn.cursor()
		cursor.execute('insert into users values ('+follower+','+followed+')')
		
	def pararDeSeguir(self, follower, followed):
		cursor = self.conn.cursor()
		cursor.execute('delete from users where follower = '+follower+' and followed = '+followed)