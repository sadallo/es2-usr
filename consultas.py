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

	def getuser(self, identificador):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM users WHERE id = {}".format(identificador)
		cursor.execute(sql)
		records = cursor.fetchall()
		if len(records) == 0:
			return ""
		else:
			return str(records[0])


	def cadastrar(self, login, name, bio):
		cursor = self.conn.cursor()
		sql = "INSERT INTO users (login, name, bio) VALUES ('{}', '{}', '{}')".format(login, name, bio)
		cursor.execute(sql)
		self.conn.commit()
		

	def remover(self, identificador):
		cursor = self.conn.cursor()
		sql = "DELETE FROM users WHERE id = {}".format(identificador)
		cursor.execute(sql)
		self.conn.commit()


	def follow(self, follower, followed):
		cursor = self.conn.cursor()
		sql = "INSERT INTO follows VALUES ({}, {}) ON CONFLICT (follower, followed) DO NOTHING".format(follower, followed)
		cursor.execute(sql)
		self.conn.commit()
		

	def unfollow(self, follower, followed):
		cursor = self.conn.cursor()
		sql = "DELETE FROM follows WHERE follower = {} AND followed = {}".format(follower, followed)
		cursor.execute(sql)
		self.conn.commit()


	def users(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM users"
		cursor.execute(sql)
		records = cursor.fetchall()
		return str(records)

	def follows(self):
		cursor = self.conn.cursor()
		sql = "SELECT * FROM follows"
		cursor.execute(sql)
		records = cursor.fetchall()
		return str(records)