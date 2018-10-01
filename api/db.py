import psycopg2

class DB():
	def __init__(self,user,password,host,dbname):
		try:
			self.conn=psycopg2.connect(host="localhost",password="Adeo256.",user="postgres",dbname="fastfoodapi")
			print('connected to {}'.format(dbname))
		except(Exception, psycopg2.DatabaseError) as e:
			print(e)
			print('Dont Panic Connection Failed')
