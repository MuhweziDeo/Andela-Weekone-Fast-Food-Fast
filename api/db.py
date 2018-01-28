import psycopg2


class DB():

    def __init__(self, user, password, host, dbname):
        try:
            self.conn = psycopg2.connect(
                host="localhost", password="Adeo256.", user="postgres", dbname="fastfoodapi")
            self.cur=self.conn.cursor()
            self.autocommit=True
            print('connected to {}'.format(dbname))
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            print('Dont Panic Connection Failed')

    def create_db_tables(self):
        queries = (

            """
            CREATE TABLE IF not EXISTS  fastfoods(
              meal_id serial ,
              meal_name varchar(20) not null primary key unique,
              price int not null 
            );
            """,
            """
            CREATE TABLE IF not EXISTS  users(
              user_id serial primary key,
              username varchar(25) not null unique,
              password varchar(100) not null,
              admin boolean default false
              
            );
            """,

            """
            CREATE TABLE IF not EXISTS orders(
              orderid serial primary key,
              user_id int not null,
              meal_name varchar(20) not null,
              location varchar(1000) not null,
              quantity int not null,
              status varchar(20) not null default 'NEW',
              order_date varchar(40) not null,
              FOREIGN KEY (meal_name) REFERENCES fastfoods(meal_name) ON DELETE CASCADE,
              FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
              
            );

            """
        )
        try:
        	for query in queries:
        		self.cur.execute(query)
        		self.conn.commit()
        		print('Tables Created')
        except(Exception, psycopg2.DatabaseError) as e:
        	print(e, "Table creation failed")

# db=DB(host="localhost", password="Adeo256.", user="postgres", dbname="fastfoodapi")
# db.create_db_tables()