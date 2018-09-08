from flask import Flask
from flask_restplus import Api


app = Flask(__name__)
api=Api(app, prefix="fastfoods/api/v1")


if __name__=='__main__':
	app.run(debug=True)